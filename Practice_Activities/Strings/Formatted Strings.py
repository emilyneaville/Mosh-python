first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
print(message)

# The above (concatenation) is not ideal. We want to use a formatted string prefixed with f'':
msg = f'{first} [{last}] is a coder'
print(msg)
# Curly brackets define placeholders in our string
# When we run our program, the holes will be filled with the value of our variable
# Useful in situations where you want to dynamically insert values into our strings
