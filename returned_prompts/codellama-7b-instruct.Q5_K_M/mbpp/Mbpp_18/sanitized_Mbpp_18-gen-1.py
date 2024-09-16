def remove_dirty_chars(first_string, second_string):
    return ''.join([char for char in first_string if char not in second_string])