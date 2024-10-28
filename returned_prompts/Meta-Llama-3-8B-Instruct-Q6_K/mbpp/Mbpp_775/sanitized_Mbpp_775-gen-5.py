def odd_position(lst):
    return all(lst[i] % 2 != 0 for i in range(1, len(lst), 2))  # Check if all elements at odd indices are odd. 