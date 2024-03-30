def compute_tax(income, credits):
    net = income - credits
    if net < 50000:
        return net * 0.15
    elif net < 100000:
        return net * 0.20
    return net * .25

def calculate_monthly_payment(amount, years, interest_rate):
    monthly_interest = interest_rate / 12                   
    months = years * 12                                
    top = amount * ( monthly_interest * (1 + monthly_interest)**months )
    monthly_payment = top / ( (1 + monthly_interest)**months - 1 )
    return monthly_payment  

def main():
    salary      = int(input('How much money did you make this year? '))
    user_credit = int(input('How much tax credit do you have? '))
    mortgage    = int(input('How much is your mortgage? '))
    years       = int(input('How many years is your mortgage? '))
    interest    = float(input('What is your mortgage interest rate? '))

    result = compute_tax(salary, user_credit)
    print('You owe $' + str(result) + ' in taxes.')

    result = calculate_monthly_payment(mortgage, years, interest)
    print('Your mortgage payment should be $' + str(result) + ' per month.')

main()