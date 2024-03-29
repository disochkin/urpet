import math


def check_number_is_power_of_two(number):
    if number <= 0:
        return False
    return math.floor(math.log2(number)) == math.ceil(math.log2(number))


if __name__ == '__main__':
    input_number = float(input('Введите число: '))
    is_power_of_two = check_number_is_power_of_two(input_number)
    if is_power_of_two:
        print(f'Число {input_number} является степенью 2')
    else:
        print(f'Число {input_number} не является степенью 2')
