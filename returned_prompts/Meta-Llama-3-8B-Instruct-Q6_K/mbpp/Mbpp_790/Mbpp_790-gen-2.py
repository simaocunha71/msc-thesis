```
def even_position(lst):
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            return False
    return True
```


This function iterates over the list with a step size of 2, meaning it checks every even index. If it finds an index where the value is not even (i.e., the remainder when divided by 2 is not 0), it immediately returns `False`. If it checks all the even indices and doesn't find any with an odd value, it returns `True`. This is based on the unit test `assert even_position([3,2,1]) == False`, which means that if the list contains at least one odd number at an even index, the function should return `False`. If the list contains only even numbers at even indices, the function should return `True`. 

The function `even_position` does exactly this and is designed to work with any list of integers. It does not have any specific requirement for the input list, other than that it is a list of integers. It also does not modify the input list in any way. It simply checks the list and returns a boolean value indicating whether the condition is met. 

This function is also quite efficient, as it only needs to check every other element in the list, which is O(n/2), or O(n) in big O notation. This is much faster than checking every element in the list, which would be O(n). 

The unit test `assert even_position([3,2,1]) == False` shows that the function should return `False` if there is at least one odd number at an even index, and the test `assert even_position([2,4,6]) == True` shows that the function should return `True` if all the even indices contain even numbers. 

The function `even_position` is designed to work with lists of integers, and it does not have any specific requirements for the input list, other than that it is a list of integers. It does not modify the input list in any way. It simply checks the list and returns a boolean value indicating whether the condition is met. 

This function is also quite efficient, as it only needs to check every other element in the list, which is O(n/2), or O(n) in big O notation. This is much faster than checking every element in the list, which would be O(n). 

The unit test `