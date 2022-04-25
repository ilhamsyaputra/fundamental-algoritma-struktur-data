from tracemalloc import start


def sort(input_array):
    unordered = len(input_array) - 1

    while unordered >= 0:
        i = 0

        while i < unordered:
            if input_array[i] > input_array[i+1]:
                input_array[i], input_array[i+1] = input_array[i+1], input_array[i]
            
            i += 1
        
        unordered -= 1

    return input_array

def selection_sort(input_array):
    array_size = len(input_array)

    for i in range(array_size):
        lowest_value_index = i

        for j in range(i+1, array_size):
            if input_array[j] < input_array[lowest_value_index]:
                lowest_value_index = j

        input_array[i], input_array[lowest_value_index] = input_array[lowest_value_index], input_array[i]
    return input_array

def insertion_sort(input_array):
    pass
