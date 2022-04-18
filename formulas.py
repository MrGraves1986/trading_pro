# def porto_risk(account_size, total_risk_percent):
#     porto_risk = account_size * total_risk_percent
#     return porto_risk

# # x = porto_risk(1000, .5)
# # print(x)    
    

# def profit_per_share(take_profit, entry):
#     profit_per_share = take_profit - entry
#     return profit_per_share

# # y = profit_per_share(6.5, 5)
# # print(y)

# def stop_loss_per_share(entry, stop_loss_price):
#     stop_loss_per_share = entry - stop_loss_price
#     return stop_loss_per_share

# # x = stop_loss_per_share(5, 4.5)
# # print(x)    

# def risk_reward_ratio(profit_per_share, stop_loss_per_share):
#     risk_reward_ratio = profit_per_share / stop_loss_per_share
#     return risk_reward_ratio

# # x = risk_reward_ratio(1.2, .39)
# # print(x)    

# def return_on_trade(take_profit, entry):
#     return_on_trade = (take_profit - entry) / entry
#     return return_on_trade

# x = return_on_trade(1.5, 1.23)
# print(x)    


# On all these, double check input name against parameters since these will need to be recognized and called.

def master(account_size,total_risk_percent, entry, stop_loss, take_profit):
    portfolio_risk_dollar_amount = account_size * total_risk_percent
    profit_per_share = take_profit - entry
    stop_loss_per_share = entry - stop_loss
    risk_to_reward_ratio = profit_per_share / stop_loss_per_share
    return_on_trade = (take_profit - entry) / entry
    ideal_position_size = portfolio_risk_dollar_amount / stop_loss_per_share
    total_position_size = ideal_position_size * entry
    
    return profit_per_share, stop_loss_per_share, risk_to_reward_ratio, return_on_trade, ideal_position_size, total_position_size

    



