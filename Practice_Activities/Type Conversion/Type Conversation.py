# Want to find the age of the user
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2022 - int(birth_year)
print(type(age))
print(age)
# This presents us with an error message
# We cannot subtract an integer (2022) and a string (birth_year)
# Need to convert birth_year into an integer using int(birth_year) in line 2
