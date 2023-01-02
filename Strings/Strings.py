course = 'Python for beginners'
print(course)
# To include an apostrophe in a string, use double quotes
course = "Python's for beginners"
print(course)
# To include double quotes in a string, use apostrophe
course = 'Python for "Beginners"'
print(course)

# What if we want to define a string that is multiple lengths? Add three quotes
course = '''
Hi John,

Here is our first email to you.

Thank you,
The support team

'''
print(course)

# We can use square brackets to get a character from a given index
course = 'Python for beginners'
#         123456789
print(course[0])
# Use negative index to get the characters starting from the end of the string
course = 'Python for beginners'
print(course[-1])

# If we want to extract multiple characters, use brackets and colon
# Be aware this excludes character at index 3 because of the way the bracket syntax works
course = 'Python for beginners'
print(course[0:3])
course = 'Python for beginners'
print(course[0:])
course = 'Python for beginners'
print(course[4:8])
course = 'Python for beginners'
print(course[:5])

# With the below syntax, we can basically copy a string (another is a copy of course)
course = 'Python for beginners'
another = course[:]
print(another)