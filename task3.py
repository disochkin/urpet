if __name__ == '__main__':
    input_number = input('Введите последовательность цифр: ')
    if len(set(list(input_number))) == len(list(input_number)):
        print('YES')
    else:
        print('NO')






