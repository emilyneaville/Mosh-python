course = 'Python for Beginners'
print(len(course))
# len() counts the number of characters in our string

# Use . to access all functions (technical term "methods") that are specific to strings
course = 'Python for Beginners'
print(course.upper())
# Notice this does not return our original string, it creates a new one

print(course.lower())

# To return the index of a specific character use .find
print(course.find('P'))
print(course.find('Beginners'))

# Method for replacing a character or a sequence of characters: .replace
print(course.replace('Beginners', 'Absolute Beginners'))
print(course.replace('P', 'J'))

# Check the existence of a character/sequence of characters in a string using "in" operator
course = 'Python for Beginners'
print('Python' in course)
print('python' in course)
# Notice difference between this method and .find method
