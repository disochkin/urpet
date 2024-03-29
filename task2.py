import math

if __name__ == '__main__':
    input_number = int(input('Введите число: '))
    super_fact = 1
    for n in range(1, input_number+1):
        super_fact = super_fact * math.factorial(n)
    print(super_fact)



