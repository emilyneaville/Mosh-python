# If name is less than 10 characters long
# "Name must be at least 10 characters"
# Otherwise if it's more than 20 characters long
# "Name can be a maximum of 20 characters"
# Otherwise
# "Looks good!"

# My attempt
username = input('Choose username: ')
characters_long = (len(username))

if characters_long < 10:
    print('Username must at least 10 characters long')
elif characters_long > 20:
    print('Username must be a maximum of 20 characters long')
else:
    print(f'Your username is {username}')
