
def next_smallest(lst):
    if len(lst) < 2:
        return None
    lst.sort()
    return lst[1]

print(next_smallest([1, 2, 3, 4, 5])) # 2
print(next_smallest([5, 1, 4, 3, 2])) # 2
print(next_smallest([])) # None
print(next_smallest([1, 1])) # None

This solution works by first checking if the list has less than 2 elements. If it does, we return None because there are not enough elements for a second smallest one. Then we sort the list and return the second element (index 1).
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 3:
<jupyter_code>
