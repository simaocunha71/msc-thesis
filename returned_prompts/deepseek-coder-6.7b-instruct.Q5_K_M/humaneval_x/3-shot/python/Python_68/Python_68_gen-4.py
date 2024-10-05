    smallest_even_val_index = [float('inf'), float('inf')]
    for index, value in enumerate(arr):
        if value % 2 == 0 and value < smallest_even_val_index[0]:
            smallest_even_val_index = [value, index]
    return smallest_even_val_index if smallest_even_val_index[0] != float('inf') else []


