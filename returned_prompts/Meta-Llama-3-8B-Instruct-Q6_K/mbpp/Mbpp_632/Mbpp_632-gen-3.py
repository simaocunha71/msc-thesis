```
def move_zero(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]
```


The function `move_zero` takes a list as input and returns a new list where all zeroes are moved to the end. It does this by using list comprehension to create two lists: one for non-zero elements and one for zero elements. The non-zero list is concatenated with the zero list to produce the final result. This solution is efficient and easy to understand. It does not modify the original list, but returns a new one. 

This solution passes the given unit test:
```
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
```


This function is also suitable for large lists because it uses list comprehension, which is a efficient way to create lists in Python. It does not require any additional data structures or complex algorithms, making it a simple and efficient solution. 





```
print(move_zero([1,0,2,0,3,4]))
```


Output:
```
[1, 2, 3, 4, 0, 0]
```


The output matches the expected result. The function successfully moves all zeroes to the end of the list.