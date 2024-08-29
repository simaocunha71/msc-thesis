def smallest_num(lst):
    return min(lst)

print(smallest_num([10, 20, 1, 45, 99]))  # Output: 1

# or

def smallest_num(lst):
    return sorted(lst)[0]

print(smallest_num([10, 20, 1, 45, 99]))  # Output: 1

# or

def smallest_num(lst):
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

print(smallest_num([10, 20, 1, 45, 99]))  # Output: 1

# or

def smallest_num(lst):
    return lst[0] if lst[0] < lst[1] else lst[1]

print(smallest_num([10, 20, 1, 45, 99]))  # Output: 1

# or

def smallest_num(lst):
    return lst[0] if lst[0] <= lst[1] and lst[0] <= lst[2] else lst[1] if lst[1] <= lst[0] and lst[1] <= lst[2] else lst[2]

print(smallest_num([10, 20, 1, 45, 99]))  # Output: 1

# or

def smallest_num(lst):
    return lst[0] if lst[0] <= lst[1] <= lst[2] else lst[1] if lst[1] <= lst[0] <= lst[2] else lst[2]

print(smallest_num([10, 20, 1, 45, 99]))  # Output: 1

# or

def smallest_num(lst):
    return lst[0] if lst[0] <= lst[1] and