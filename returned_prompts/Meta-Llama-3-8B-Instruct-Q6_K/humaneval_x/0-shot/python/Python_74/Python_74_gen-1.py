```
def total_match(lst1, lst2):
    total1 = sum(len(s) for s in lst1)
    total2 = sum(len(s) for s in lst2)
    if total1 < total2:
        return lst1
    elif total1 > total2:
        return lst2
    else:
        return lst1
```


This function works by first calculating the total number of characters in each list using a generator expression. Then it compares these totals and returns the list with the smaller total. If the totals are equal, it returns the first list. The function is case-sensitive because it counts each character individually, including spaces and punctuation. If you want to ignore case, punctuation, and spaces, you would need to preprocess the strings to remove or normalize these characters.