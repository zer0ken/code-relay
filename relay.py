import re

while not re.compile(r'\d+').fullmatch(number := input('I think you have to insert a number in integer and press Enter key: ')):
    print('Maybe you are not getting it.')
else:
    number = int(number)

for i in range(number):
    print('Hello, world!')
