
def sort_even(l: list):
    sorted_even = sorted(l[i] for i in range(0, len(l), 2))
    return l[:len(l)//2:2] + sorted_even + l[len(l)//2:len(l):2]



# Test
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]





def sort_even(l: list):
    even_list = l[::2]
    even_list.sort()
    return l[:len(l)//2:2] + even_list + l[len(l)//2:len(l):2]

# Test
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]






def sort_even(l: list):
    even_list = sorted(l[i] for i in range(0, len(l), 2))
    return l[:len(l)//2:2] + even_list + l[len(l)//2:len(l):2]

# Test
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]







def sort_even(l: list):
    sorted_even = sorted(l[i] for i in range(0, len(l), 2))
    return l[:len(l)//2:2] + sorted_even + l[len(l)//2:len(l):2]

# Test
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(