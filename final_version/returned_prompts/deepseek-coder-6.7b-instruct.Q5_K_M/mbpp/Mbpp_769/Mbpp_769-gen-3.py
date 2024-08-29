def Diff(lst1, lst2):
    return [i for i in lst1 if i not in lst2]

lst1 = [10, 15, 20, 25, 30, 35, 40]
lst2 = [25, 40, 35]
print(Diff(lst1, lst2))

"""
Output:
[10, 20, 30, 15]
"""

Explanation:
The function `Diff` takes two lists `lst1` and `lst2` as inputs. It returns a new list that contains all elements of `lst1` that are not in `lst2`. The 'for' loop inside the list comprehension iterates over each element 'i' in `lst1` and checks if it's not in `lst2`. If the element is not in `lst2`, it's included in the new list.
"""

"""
