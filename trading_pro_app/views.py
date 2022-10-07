from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *
# import locale ***Need to explore this more and settting it up

def index(request):
    return render(request, "index.html")

def philosophy(request):
    return render(request, "philosophy.html")    

def calculate(request):
    return render(request, "calculator.html")

def risk(request):
    return render(request, "risk_management.html")   

def master(request):
    request.session['account_size'] = float(request.POST['account_size'])
    request.session['account_risk_percent'] = float(request.POST['account_risk_percent'])
    request.session['entry'] = float(request.POST['entry'])
    request.session['stop_loss'] = float(request.POST['stop_loss'])
    request.session['take_profit'] = float(request.POST['take_profit']) 

    request.session['dollar_risk_on_trade'] = format((request.session['account_size'] * request.session['account_risk_percent']), ",.2f")

    request.session['profit_per_share'] = format((request.session['take_profit']) - (request.session['entry']), ",.2f")

    request.session['stop_loss_per_share'] = format((request.session['entry']) - (request.session['stop_loss']), ".2f")

    request.session['risk_to_reward_ratio'] = float(request.session['profit_per_share']) / float(request.session['stop_loss_per_share'])

    request.session['total_risk_reward'] = str(round(request.session['risk_to_reward_ratio'], 2))

    request.session['return_on_trade'] = f"{(request.session['take_profit'] - request.session['entry']) / request.session['entry']: .2%}"

    request.session['number_of_shares'] = float(request.session['dollar_risk_on_trade']) / float(request.session['stop_loss_per_share'])

    request.session['ideal_number_of_shares'] = str(round(request.session['number_of_shares'], 2))
 
    request.session['total_position_size'] = format((request.session['number_of_shares']) * float(request.session['entry']), ",.2f")
   
    
    return redirect ('/trade_setup')


def trade_setup(request):
    return render(request, 'trade_stats.html')    

def indicators(request):
    return render(request, "indicators.html")    

def rsi(request):
    return render(request, "rsi_examples.html") 

def moving_av(request):
    return render(request, "moving_av_examples.html" )       

def ema(request):
    return render(request, "ema_examples.html")

def others(request):
    return render(request, "other_examples.html")

def journal(request):
    return render(request, "trade_log.html")