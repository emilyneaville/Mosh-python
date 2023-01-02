# Create variable is_hot; Change boolean value for different return value
is_hot = True
# Return 1st script if condition is true, return different script if not true
if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
else:
    print("It's a cold day")
    print('Wear a jacket')
print('Have a good day')

# Define another variable to implement else if one variable is not true (elif)
# Finally, implement (else) to return if neither are true
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:
    print("It's a cold day")
    print('Wear a jacket')
else:
    print("It's a lovely day")
print('Have a good day')
