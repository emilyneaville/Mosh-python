# Define 2 variables
# With "and", if both variables are true, then if
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print('Eligible for loan')
else:
    print('Not eligible for loan')

# With "or", if at least one variable is true, then if
has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
    print('Eligible for loan')
else:
    print('Not eligible for loan')

# "Not" inverses any boolean value we give it
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print('Eligible for loan')
else:
    print('Not eligible for loan')

