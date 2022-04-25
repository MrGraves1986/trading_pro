from django.db import models

class trade_setup(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    # trade_type =
    coin = models.CharField(max_length=10)
    entry = models.DecimalField(max_digits=5, decimal_places=2)
    stop_loss = models.DecimalField(max_digits=5, decimal_places=2)
    take_profit = models.DecimalField(max_digits=5, decimal_places=2)
    exit_price = models.DecimalField(max_digits=5, decimal_places=2)
    # return_on_trade = 
    

