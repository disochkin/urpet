def check_contain_redundance_digits(input_number):
    if len(set(list(input_number))) == len(list(input_number)):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    input_number = input('Введите последовательность цифр: ')
    print(check_contain_redundance_digits(input_number))

# input_number - строковый тип






