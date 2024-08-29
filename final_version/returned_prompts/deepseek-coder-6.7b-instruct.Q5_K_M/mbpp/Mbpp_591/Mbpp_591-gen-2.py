def swap_List(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

print(swap_List([12, 35, 9, 56, 24]))

# Output: [24, 35, 9, 56, 12]


# Solution 2:
def swap_List(lst):
    lst.insert(0, lst.pop(-1))
    return lst

print(swap_List([12, 35, 9, 56, 24]))

# Output: [24, 35, 9, 56, 12]


# Solution 3:
def swap_List(lst):
    lst.append(lst.pop(0))
    return lst

print(swap_List([12, 35, 9, 56, 24]))

# Output: [24, 35, 9, 56, 12]


# Solution 4:
def swap_List(lst):
    lst = [lst[-1]] + lst[1:-1] + [lst[0]]
    return lst

print(swap_List([12, 35, 9, 56, 24]))

# Output: [24, 35, 9, 56, 12]


# Solution 5:
def swap_List(lst):
    return lst[-1:] + lst[1:-1] + lst[:1]

print(swap_List([12, 35, 9, 56, 24]))

# Output: [24, 35, 9, 56, 12]
"""
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
