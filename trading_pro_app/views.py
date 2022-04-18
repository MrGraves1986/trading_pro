from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")

def philosophy(request):
    return render(request, "philosophy.html")    

def calculate(request):
    return render(request, "calculator.html")

def risk(request):
    return render(request, "risk_management.html")   


#This will need to be adjusted so the #'s from input boxes = the parameters. This is also going to redirect back to same page with results. Will need a "Clear/Reset" button feature.
def master(request):
    # context = {
    #     'entry': entry,
    #     'stop_loss': stop_loss,
    #     'take_profit': take_profit
    # }
    return render(request,"trade_stats.html")