from multiprocessing import context
from django.shortcuts import render, redirect

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

    request.session['dollar_risk_on_trade'] = float(request.session['account_size']) * float(request.session['account_risk_percent'])

    request.session['profit_per_share'] = float(request.session['take_profit']) - float(request.session['entry'])

    request.session['stop_loss_per_share'] = float(request.session['entry']) - float(request.session['stop_loss'])

    request.session['risk_to_reward_ratio'] = float(request.session['profit_per_share']) / float(request.session['stop_loss_per_share'])

    request.session['return_on_trade'] = (float(request.session['take_profit']) - float(request.session['entry'])) / float(request.session['entry'])

    request.session['number_of_shares'] = float(request.session['dollar_risk_on_trade']) / float(request.session['stop_loss_per_share'])

    request.session['total_position_size'] = float(request.session['number_of_shares']) * float(request.session['entry'])
   
    
    return redirect ('/trade_setup')


def trade_setup(request):
    return render(request, 'trade_stats.html')    