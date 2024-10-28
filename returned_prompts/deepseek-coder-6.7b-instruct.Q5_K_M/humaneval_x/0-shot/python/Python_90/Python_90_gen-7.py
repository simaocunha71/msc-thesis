
def next_smallest(lst):
    if len(lst) < 2:
        return None
    lst = list(set(lst))
    lst.sort()
    return lst[1] if len(lst) > 1 else None

print(next_smallest([1, 2, 3, 4, 5]))
print(next_smallest([5, 1, 4, 3, 2]))
print(next_smallest([]))
print(next_smallest([1, 1]))

The function first checks if the list has less than two elements. If yes, it returns None. Then it removes duplicates from the list by converting it to a set and back to a list again. It sorts the list in ascending order. If the list has more than one element, it returns the second one (index 1), otherwise it returns None.
<jupyter_output>
2
2
None
None
<jupyter_text>
Problem 2
<jupyter_code>
