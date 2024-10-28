```
def multiple_to_single(lst):
    return int(''.join(map(str, lst)))
```


The function takes a list of integers as input and returns a single integer.
The idea is to convert each integer in the list to a string, join all the strings together, and then convert the resulting string back to an integer. This is done using the map function to convert each integer to a string, the join function to concatenate all the strings together, and the int function to convert the resulting string back to an integer.

For example, if the input list is [11, 33, 50], the function will first convert each integer to a string, resulting in ['11', '33', '50']. Then it will join these strings together to get '113350'. Finally, it will convert this string back to an integer and return the result, which is 113350. This is what the unit test `assert multiple_to_single([11, 33, 50])==113350` is checking.