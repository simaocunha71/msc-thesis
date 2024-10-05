```
def total_match(lst1, lst2):
    total1 = sum(len(i) for i in lst1)
    total2 = sum(len(i) for i in lst2)
    
    if total1 < total2:
        return lst1
    elif total1 > total2:
        return lst2
    else:
        return lst1
```


Test:
```
print(total_match([], []))  # []
print(total_match(['hi', 'admin'], ['hI', 'Hi']))  # ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))  # ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))  # ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5']))  # ['4']
```


Explanation:
The function `total_match` takes two lists of strings as input. It calculates the total number of characters in each list by summing the lengths of all strings in the list. It then compares the two totals and returns the list with the smaller total. If the totals are equal, it returns the first list. The function works by iterating over each string in the list, calculating its length, and adding that to the total. It does this for both lists, then compares the results. If the first list has the smaller total, it returns that list. If the second list has the smaller total, it returns that list. If the totals are equal, it returns the first list. This function works for lists of any size, and it handles lists that are empty or contain only one string. It also handles lists that contain strings of different lengths and lists that contain strings with different characters. The function works by simply counting the number of characters in each string and adding that to the total. It does not care about the characters themselves, just the number of them. This makes it efficient and easy to use. It is also easy to understand and debug, because it does exactly what it is supposed to do. It does not have any unnecessary complexity or side effects. It simply calculates the total number of characters in each list and returns the list with the smaller total. This makes it easy to use and understand. It is also easy to test, because it does exactly what it is supposed to do. It can be tested by calling it