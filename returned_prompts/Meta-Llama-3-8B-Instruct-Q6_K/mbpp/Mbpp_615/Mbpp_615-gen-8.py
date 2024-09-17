```
def average_tuple(tuples):
    return [sum(t)/len(t) for t in tuples]
```
This function uses a list comprehension to iterate over each tuple in the input list. For each tuple, it calculates the average value by summing all the elements in the tuple and dividing by the number of elements. The results are returned as a list. The unit test provided helps to clarify the expected output. For example, the test `assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]` shows that the function should return a list with the average values for each tuple. 

This function assumes that all tuples have the same number of elements. If the tuples can have different numbers of elements, you would need to add error checking to handle this. For example, you could calculate the length of the first tuple and then use that length for all the other tuples, or you could raise an exception if the lengths are different. 

In this case, the function will work correctly as long as all tuples have the same number of elements. If a tuple has zero elements, the function will raise a ZeroDivisionError when it tries to divide by the length of the tuple. If you want to handle this case, you could add a check to return a special value (such as None) or raise a custom exception when the length of a tuple is zero. 

This function also assumes that the input is a tuple of tuples. If the input could be a list of lists or a list of tuples, you would need to add error checking to handle this. For example, you could use the isinstance function to check if the input is a tuple of tuples, and raise an exception if it's not. 

Here is the updated function that handles these cases:
```
def average_tuple(tuples):
    if not isinstance(tuples, tuple):
        raise ValueError("Input must be a tuple of tuples")
    for t in tuples:
        if not isinstance(t, tuple):
            raise ValueError("Input must be a tuple of tuples")
        if len(t) == 0:
            raise ValueError("Tuple cannot have zero elements")
    return [sum(t)/len(t) for t in tuples]
```  This function will now correctly handle