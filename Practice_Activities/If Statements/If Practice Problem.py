# Price of a house is $1M
# If the buyer has good credit, they have to put down 10% of the property
# If the buyer has bad credit, they have to put down 20% of the property

# My solution
price = 1000000
good_credit = True
bad_credit = False
if good_credit:
    print('The buyer has good credit')
    down_payment = price * .1
    print('The down payment is $' + str(down_payment))
else:
    print('The buyer has bad credit')
    down_payment = price * .2
    print('The down payment is $' + str(down_payment))

# Mosh solution
price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'Down payment: ${down_payment}')

# My new solution - Used formatted string
price = 1000000
good_credit = False

if good_credit:
    print('The Buyer has good credit')
    down_payment = price * .1
    print(f'Down payment: ${down_payment}')
else:
    print('The buyer has bad credit')
    down_payment = price * .2
    print(f'Down payment: ${down_payment}')
