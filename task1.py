def get_digit_count(row):
    only_digit = input_row.replace('.', '').replace('-', '')
    return len(only_digit)


if __name__ == '__main__':
    input_row = input('Введите число: ')
    digits_count = get_digit_count(input_row)
    print(f'Кол-во цифр в записи числа: {digits_count}')


# input_row - строковый тип
# only_digit - строковый тип
# digits_count - целочисленный тип

