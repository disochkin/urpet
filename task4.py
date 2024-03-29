def get_min_number_position(number_array):
    index_of_min_item = 0
    for index in range(0, len(number_array)):
        if number_array[index] < number_array[index_of_min_item]:
            index_of_min_item = index
    return index_of_min_item

def get_max_number_position(number_array):
    index_of_max_item = 0
    for index in range(0, len(number_array)):
        if number_array[index] > number_array[index_of_max_item]:
            index_of_max_item = index
    return index_of_max_item

def swap_positions(number_array, pos1, pos2):
    number_array[pos1], number_array[pos2] = number_array[pos2], number_array[pos1]
    return number_array

def get_swapped_min_max_array(number_array):
    min_value_index = get_min_number_position(number_array)
    max_value_index = get_max_number_position(number_array)
    return swap_positions(number_array, min_value_index, max_value_index)

if __name__ == '__main__':
    number_array = list()
    number_array_length = int(input('Введите кол-во цифр: '))
    for i in range(1, number_array_length+1):
        new_item = float(input(f'Введите элемент {i} из {number_array_length}: '))
        number_array.append(new_item)
    print(get_swapped_min_max_array(number_array))

# number_array - список
# number_array_length - целочисленный тип
# new_item - с плавающей запятой
# index_of_min_item - целочисленный тип
# index_of_max_item - целочисленный тип

