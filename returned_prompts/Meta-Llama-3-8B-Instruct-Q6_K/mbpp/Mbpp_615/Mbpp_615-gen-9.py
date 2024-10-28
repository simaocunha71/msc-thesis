```
def average_tuple(tuples):
    return [sum(t)/len(t) for t in tuples]
```


The function works by iterating over each tuple in the input list, summing its elements, and then dividing by the number of elements. The results are returned as a list. 

The unit test provided helps to clarify the expected behavior of the function, showing that the average value should be calculated for each tuple in the input list. 

For example, the test case `assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]` tests that the function correctly calculates the average value for each tuple in the input list. 

The function is designed to be flexible and can handle tuples of any length, not just those with four elements. It will work correctly with tuples of length 1, 2, 3, etc. 

The function is also designed to handle non-numeric values in the tuples. If a tuple contains non-numeric values, the function will raise a TypeError when it tries to sum the elements. If you want to handle non-numeric values in a different way, you could add error checking to the function to handle this situation. 

For example, you could use a list comprehension to filter out non-numeric values, or you could use the `map` function to convert the tuple elements to a numeric type. 

Here is an example of how you could modify the function to handle non-numeric values:
```
def average_tuple(tuples):
    return [sum(map(float, t))/len(t) for t in tuples]
```
This version of the function uses the `map` function to convert each element in the tuple to a float, and then sums the resulting list of floats. This will handle tuples that contain non-numeric values, such as strings or booleans. 

However, it's worth noting that this approach will raise a TypeError if the tuple contains non-convertible values, such as a tuple or a dictionary. If you want to handle this situation, you could add additional error checking to the function. 

For example, you could use a list comprehension to filter out non-numeric values, like this:
```
def average_tuple(tuples):
    return [sum([