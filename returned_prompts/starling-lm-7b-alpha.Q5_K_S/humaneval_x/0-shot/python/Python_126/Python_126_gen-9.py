    # Here's a possible solution using list comprehension
    return len(set(lst)) == len(lst)

# Here's a possible solution using for loop
# def is_sorted(lst):
#     for i in range(len(lst)-1):
#         if lst[i+1] < lst[i]:
#             return False
#     return True

# Here's a possible solution using built-in sorted function
# def is_sorted(lst):
#     return lst == sorted(lst)





# Here's some testing
print(is_sorted([5]))  # True
print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([1, 3, 2, 4, 5]))  # False
print(is_sorted([1, 2, 3, 4, 5, 6]))  # True
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))  # True
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))  # False
print(is_sorted([1, 2, 2, 3, 3, 4]))  # True
print(is_sorted([1, 2, 2, 2, 3, 4]))  # False







```
