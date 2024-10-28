```
def check_type(t):
    return len(set(type(i) for i in t)) == 1
```
The function takes a tuple t as input and returns True if all elements in the tuple are of the same type, False otherwise.

It uses a generator expression to get the type of each element in the tuple, converts the generator to a set (which removes duplicates), and checks if the length of the set is 1. If it is, then all elements are of the same type, and the function returns True. Otherwise, it returns False.

The unit test `assert check_type((5, 6, 7, 3, 5, 6)) == True` is passed because all the elements in the tuple are integers, so the function returns True. 