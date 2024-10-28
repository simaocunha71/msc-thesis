```
def count_Occurrence(tup, lst):
    count_dict = {}
    for i in tup:
        if i in lst:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
    return sum(count_dict.values())
```

This function works by iterating over the tuple and checking if each element is in the list. If it is, it increments the count for that element in the dictionary. Finally, it returns the sum of the counts in the dictionary. The unit test `assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3` ensures that the function works correctly. 
However, this function counts all occurrences of elements in the tuple, not just the ones in the list. So, for example, if the tuple is ('a', 'a', 'c', 'b', 'd') and the list is ['a', 'b'], the function will return 4, not 3. To fix this, we can modify the function to only count the occurrences of elements that are in the list. Here is the modified function:

```
def count_Occurrence(tup, lst):
    count_dict = {}
    for i in lst:
        count_dict[i] = tup.count(i)
    return sum(count_dict.values())
```

This function works by iterating over the list and using the count method of the tuple to count the occurrences of each element in the tuple. It then returns the sum of these counts. This function will return the correct result for the unit test `assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3`. 