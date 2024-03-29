home_cost = int(input('How much does the home cost? '))
available_funds = int(input('How much money do you have immediately available? '))
down_payment = home_cost * 0.2
if available_funds >= down_payment:
    print('You can afford the down payment!')
else: 
    print('baisé')