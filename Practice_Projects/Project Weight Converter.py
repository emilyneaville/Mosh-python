# Be able to convert a user's weight into kilos or pounds

weight = int(input('What is your weight? '))
unit = input('(K)g or (L)bs? ')

if unit.upper() == 'L':
    print(f'Your weight in kg is {int(weight) * 0.45}')
elif unit.upper() == 'K':
    print(f'Your weight in lbs is {int(weight) / 0.45}')

# Again

weight = int(input('Weight: '))
unit = input('Lbs or kg? ')

if unit.