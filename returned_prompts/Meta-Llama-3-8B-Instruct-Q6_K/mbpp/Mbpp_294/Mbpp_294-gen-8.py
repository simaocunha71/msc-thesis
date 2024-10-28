```
def max_val(lst):
    return max(map(int, [i for i in lst if isinstance(i, int)]))
```


This function works by first filtering the list to only include the integers using a list comprehension and the isinstance function. It then converts these integers to a list and finds the maximum value in this list using the built-in max function.

The unit test provided, assert max_val(['Python', 3, 2, 4, 5, 'version'])==5, shows that the function should return the maximum integer value in the list. The function passes this test because it correctly identifies the maximum integer value in the list as 5.