```
def sum_negativenum(lst):
    return sum(num for num in lst if num < 0)
``` 
The function `sum_negativenum` takes a list of numbers `lst` as input and returns the sum of all negative numbers in the list. It uses a generator expression to iterate over the list and sum up the negative numbers. The `assert` statement checks if the function returns the correct result for the given input.