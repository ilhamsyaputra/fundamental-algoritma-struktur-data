def linear_search(input_array, search_value):
    for index, value in enumerate(input_array):
        if value == search_value:
            return index