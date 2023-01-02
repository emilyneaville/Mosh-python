# Input function will print this message on a terminal
name = input('What is your name? ')
# Function then waits for input from user, then stores it as a variable "name"
print('Hi ' + name)

# Exercise: Extend this program and ask two more questions
favorite_color = input(name + ', What is your favorite color? ')
print('Okay ' + name + ', your favorite color is ' + favorite_color)

emotion = input(name + ', how does ' + favorite_color + ' make you feel? ')
print(favorite_color + ' makes you feel ' + emotion)

# Again, differently
name = input('What is your name? ')
favorite_color = input('What is your favorite color? ')
emotion = input('How does this color make you feel? ')
print('Hi '+ name)
print(name + ' likes ' + favorite_color)
print(favorite_color + ' makes ' + name + ' feel ' + emotion)
