import math


def get_super_fact(number):
    super_fact = 1
    for n in range(1, number + 1):
        super_fact = super_fact * math.factorial(n)
    return super_fact


if __name__ == '__main__':
    input_number = int(input('Введите число: '))
    print(f'Суперфакториал для n={input_number} = {get_super_fact(input_number)}')

# input_number - целочисленный тип
# n - целочисленный тип
# number - целочисленный тип
# super_fact - целочисленный тип
