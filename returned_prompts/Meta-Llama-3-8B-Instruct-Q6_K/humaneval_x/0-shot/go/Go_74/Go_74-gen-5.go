Here is the Python solution:
```
def TotalMatch(lst1, lst2):
    total_chars1 = sum(len(s) for s in lst1)
    total_chars2 = sum(len(s) for s in lst2)
    if total_chars1 < total_chars2:
        return lst1
    elif total_chars1 > total_chars2:
        return lst2
    else:
        return lst1
```
Here's how it works:

1. We calculate the total number of characters in each list using a generator expression that sums up the lengths of the strings in each list.
2. We compare the total number of characters in each list. If `lst1` has fewer characters, we return `lst1`. If `lst2` has fewer characters, we return `lst2`.
3. If the two lists have the same number of characters, we return `lst1` (since the problem statement says to return the first list in case of a tie).

You can test this function with the examples you provided to see that it returns the correct result. Let me know if you have any questions or need further clarification! 😊
```
print(TotalMatch([], []))  # []
print(TotalMatch(['hi', 'admin'], ['hI', 'Hi']))  # ['hI', 'Hi']
print(TotalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))  # ['hi', 'admin']
print(TotalMatch(['hi', 'admin'], ['hI', 'hi', 'hi']))  # ['hI', 'hi', 'hi']
print(TotalMatch(['4'], ['1', '2', '3', '4', '5']))  # ['4']
```
Let me know if you have any other questions! 😊
```
print(TotalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project', 'hi']))  # ['hi', 'admin']
print(TotalMatch(['hi', 'admin'], ['hi', 'hi', 'hi', 'admin']))  # ['hi', 'admin']
print(TotalMatch(['hi', 'admin'], ['hi', 'hi', 'hi', 'hi']))  # ['hi', 'admin']
print(TotalMatch(['hi', 'admin'], ['hi', 'hi', 'hi', 'hi', 'hi']))  # ['hi', 'admin']
```
Let me know if you