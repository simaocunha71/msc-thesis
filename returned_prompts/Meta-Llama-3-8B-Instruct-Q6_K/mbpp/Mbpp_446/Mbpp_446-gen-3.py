```
def count_Occurrence(tup, lst):
    count = {}
    for i in tup:
        if i in lst:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
    return sum(count.values())
```
This function iterates over the tuple and counts the occurrences of elements in the tuple that are also in the list. The result is the sum of these occurrences. The unit test `assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3` ensures that the function works correctly. 

The function uses a dictionary `count` to keep track of the occurrences of each element. The `values()` method of the dictionary is used to get a list of the values, which are then summed using the `sum()` function. 

The time complexity of this function is O(n), where n is the length of the tuple, because it needs to iterate over the tuple once. The space complexity is also O(n), because in the worst case, all elements of the tuple are in the list and the dictionary needs to store all of them. 







