```
def get_equal(tuples):
    return len(set(len(t) for t in tuples)) == 1
```
The problem is asking to write a function that checks if all the given tuples have the same length or not. 

The unit test `assert get_equal([(11, 22, 33), (44, 55, 66)]) == True` suggests that the function should return `True` if all tuples have the same length, and `False` otherwise.

We can solve this problem by using a set comprehension to find the length of each tuple in the list, and then check if the length of this set is 1. If it is 1, it means all tuples have the same length, and we return `True`. Otherwise, we return `False`.

Here is the Python code that implements this idea:
```
def get_equal(tuples):
    return len(set(len(t) for t in tuples)) == 1
```
This function uses a set comprehension to find the length of each tuple in the list, and then checks if the length of this set is 1. If it is 1, it means all tuples have the same length, and we return `True`. Otherwise, we return `False`.