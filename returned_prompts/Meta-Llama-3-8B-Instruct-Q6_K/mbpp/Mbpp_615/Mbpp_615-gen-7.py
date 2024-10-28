```
def average_tuple(tuples):
    result = []
    for t in tuples:
        avg = sum(t) / len(t)
        result.append(avg)
    return result
```


This function iterates over each tuple in the input list of tuples. For each tuple, it calculates the average by summing all the values and dividing by the length of the tuple. The calculated average is then appended to the result list. The function finally returns the list of averages.

The unit test provided in the problem statement is:
```
assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]
```
This test checks that the function correctly calculates the average for each tuple in the input list. The expected output is a list of averages, which is `[30.5, 34.25, 27.0, 23.25]`. The function should return the same output for the given input. If the function returns the correct output, the test passes; otherwise, it fails.