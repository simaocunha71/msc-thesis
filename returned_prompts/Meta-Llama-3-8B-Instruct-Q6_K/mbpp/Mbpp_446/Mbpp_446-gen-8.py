```
def count_Occurrence(tuple_list, elements):
    count = 0
    for element in elements:
        for item in tuple_list:
            if item == element:
                count += 1
    return count
```
This function takes a tuple and a list as input. It then iterates over the list of elements and for each element, it iterates over the tuple, counting the occurrences of that element. The function finally returns the total count.

For example, if we call `count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b'])`, it will return `3` because 'a' occurs 2 times and 'b' occurs 1 time in the tuple. 