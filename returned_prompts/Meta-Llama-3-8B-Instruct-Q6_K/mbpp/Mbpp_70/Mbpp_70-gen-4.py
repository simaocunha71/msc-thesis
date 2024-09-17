```
def get_equal(tuples):
    return len(set(map(len, tuples))) == 1
```
This function uses the built-in functions set and map to get the lengths of all tuples in the given list. The set function converts the map object into a set, which removes duplicate elements. If all tuples have equal length, the set will contain only one element, which is the length of the tuples. If there are multiple elements in the set, it means that the tuples have different lengths. The function returns True if all tuples have equal length and False otherwise.  



This function is tested with the given unit test:
```
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
```
which passes, indicating that the function works correctly.  



Note that this function assumes that the input is a list of tuples. If the input can be any iterable of iterables, you would need to add some error checking code to handle that.  



Also, this function returns True if all tuples have equal length, and False otherwise. If you want to return the length of the tuples if they are all equal, you would need to add some additional code to handle that.  



Here's a breakdown of how the function works:

1. `map(len, tuples)`: This applies the `len` function to each tuple in the list. The result is a map object that contains the lengths of all tuples.
2. `set(...)`: This converts the map object into a set, which removes duplicate elements.
3. `len(set(...)) == 1`: This checks if the set contains only one element. If it does, it means that all tuples have equal length, and the function returns True. If the set contains more than one element, it means that the tuples have different lengths, and the function returns False.  



This function is efficient because it uses built-in functions that are implemented in C, which makes it faster than a naive implementation that uses a loop. It is also easy to understand and modify, which makes it a good choice for a production environment.  



However, it's worth noting that this function assumes that the input is a list of tuples. If the input can be any iterable of iterables, you would need to add some error checking code to handle that. For example, you could add a check to make sure that all elements of the input are tuples, and raise an exception if they are not.  