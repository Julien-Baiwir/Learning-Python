income = int(input('net:'))
credits = int(input('credits:'))

def compute_tax(income, credits):
    net = income - credits
    if net < 50000:
        return net * 0.15
    elif net < 100000:
        return net * 0.20
    return net * .25

result = compute_tax(income, credits)
print("Tax to be paid:", result)