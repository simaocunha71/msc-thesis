def add_n_to_elements(lst, n):
    return [i + n for i in lst]

print(add_n_to_elements([1, 2, 3, 4, 5], 5))

"""
Write a function that takes in a list of numbers and returns a new list with the elements in reverse order.
assert reverse_list([1, 2, 3, 4, 5])==[5, 4, 3, 2, 1]