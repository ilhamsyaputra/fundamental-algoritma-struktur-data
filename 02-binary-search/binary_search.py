def binary_search(input_array, search_value):
    lower_bound = 0
    upper_bound = len(input_array) - 1

    while lower_bound <= upper_bound:
        midpoint = (lower_bound + upper_bound) // 2

        if input_array[midpoint] == search_value:
            return midpoint
        elif input_array[midpoint] < search_value:
            lower_bound = midpoint + 1
        elif input_array[midpoint] > search_value:
            upper_bound = midpoint - 1

