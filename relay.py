import re

NUMBER_RE = re.compile(r'\d+')


def get_number():
    return input('I think you have to insert a number in integer and press Enter key: ')


def main():
    while not NUMBER_RE.fullmatch(number := get_number()):
        print('Maybe you are not getting it.')
    else:
        number = int(number)

    for i in range(number):
        print('Hello, world!')


if __name__ == '__main__':
    main()
