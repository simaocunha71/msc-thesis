```
def sum_of_digits(lst):
    return sum(sum(int(digit) for digit in str(num)) for num in lst)
```


In this problem, we need to write a function that takes a list of numbers as input and returns the sum of the digits of each number in the list.

The unit test provided, `assert sum_of_digits([10,2,56])==14`, helps us understand how the function should work. It shows that the function should sum the digits of each number in the list and return the total sum.

Here is the solution:
```
def sum_of_digits(lst):
    return sum(sum(int(digit) for digit in str(num)) for num in lst)
```
This function uses a generator expression to convert each number in the list to a string, then iterate over each character in the string, convert it back to an integer, and sum them up. The outer `sum` function then adds up these sums for each number in the list.

For example, if we call `sum_of_digits([10,2,56])`, the function will first convert each number to a string: `['10', '2', '56']`. Then, it will iterate over each character in each string, convert it back to an integer, and sum them up: `1+0+2+5+6=14`. Finally, it will return the total sum, which is `14`.