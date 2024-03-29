import math

if __name__ == '__main__':
    input_number = input('Введите число: ')
    try:
        positive_number = abs(int(input_number))
        digits = 1 + math.floor(math.log10(positive_number))
        print(f'Кол-во цифр в записи числа: {digits}')
    except ValueError:
        if not input_number:
            raise ValueError('Пустая строка!')
        else:
            raise ValueError(f'Строка "{input_number}" не является числом!')
