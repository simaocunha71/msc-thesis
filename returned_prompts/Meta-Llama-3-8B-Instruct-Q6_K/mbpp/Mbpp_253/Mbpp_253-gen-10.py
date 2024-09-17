```
def count_integer(lst):
    return len([i for i in lst if isinstance(i, int)])
```
This function uses a list comprehension to create a new list that only includes the elements in the original list that are integers. It then returns the length of this new list, which is the number of integer elements in the original list.

The unit test `assert count_integer([1,2,'abc',1.2]) == 2` ensures that the function correctly identifies the two integer elements (1 and 2) in the list, and ignores the non-integer elements ('abc' and 1.2). 