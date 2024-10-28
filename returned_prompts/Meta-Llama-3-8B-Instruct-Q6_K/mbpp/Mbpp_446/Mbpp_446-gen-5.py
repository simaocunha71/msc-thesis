```
def count_Occurrence(t, lst):
    occurrence = {}
    for i in t:
        if i in lst:
            if i in occurrence:
                occurrence[i] += 1
            else:
                occurrence[i] = 1
    return sum(occurrence.values())
```
Explanation: 
This function takes a tuple `t` and a list `lst` as arguments. It initializes an empty dictionary `occurrence` to store the occurrence of each element in `lst` in `t`. It then iterates over each element `i` in `t`. If `i` is in `lst`, it checks if `i` is already in `occurrence`. If it is, it increments the count by 1; otherwise, it sets the count to 1. Finally, it returns the sum of the values in `occurrence`, which represents the total occurrence of elements in `lst` in `t`. The unit test `assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3` ensures that the function works correctly. For example, in this test, the function should return 3 because 'a' appears twice and 'b' appears once in the tuple `('a', 'a', 'c', 'b', 'd')`. 