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
    request.session['account_size'] = request.POST['account_size']
    request.session['account_risk_percent'] = request.POST['account_risk_percent']
    request.session['entry'] = request.POST['entry']
    request.session['stop_loss'] = request.POST['stop_loss']
    request.session['take_profit'] = request.POST['take_profit'] 

    request.session['profit_per_share'] = int(request.session['take_profit']) - int(request.session['entry'])

    request.session['stop_loss_per_share'] = int(request.session['entry']) - int(request.session['stop_loss'])

    request.session['risk_to_reward_ratio'] = int(request.session['profit_per_share']) / int(request.session['stop_loss'])

    request.session['return_on_trade'] = (int(request.session['take_profit']) - int(request.session['entry']) / int(request.session['entry']))

    request.session['total_position_size'] = int(request.session['account_risk_percent']) / int(request.session['stop_loss_per_share'])


    # profit_per_share = request.session['take_profit'] - (request.session['entry']
    # stop_loss_per_share = request.session['entry'] - request.session['stop_loss']
    # risk_to_reward_ratio =  profit_per_share / stop_loss_per_share
    # return_on_trade = request.session['take_profit'] - request.session['entry'] / request.session['entry']
    # total_position_size = request.session['account_risk_percent'] / 'stop_loss_per_share'
   
    
    return redirect ('/trade_setup')


def trade_setup(request):
    return render(request, 'trade_stats.html')    