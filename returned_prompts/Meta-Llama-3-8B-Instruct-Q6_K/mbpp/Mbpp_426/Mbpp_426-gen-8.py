```
def filter_oddnumbers(lst):
    return [i for i in lst if i % 2 != 0]
```


The unit test `assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]` suggests that the function should return a list of odd numbers from the given list. 

We can use a list comprehension to achieve this. The condition `i % 2 != 0` filters out even numbers, leaving only the odd numbers in the list. The function takes a list as input and returns a list of odd numbers. 

For example, if we call `filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])`, it will return `[1,3,5,7,9]`. 

This solution is concise, readable, and efficient, making it a good choice for this problem. 