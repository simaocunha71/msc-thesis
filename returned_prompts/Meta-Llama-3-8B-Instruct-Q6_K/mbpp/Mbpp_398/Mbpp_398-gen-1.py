```
def sum_of_digits(lst):
    return sum(sum(int(digit) for digit in str(num)) for num in lst)
```


The function `sum_of_digits` takes a list of integers as input and returns the sum of the digits of each number in the list. It achieves this by using a generator expression to sum the digits of each number in the list, and then summing these results together. The `str` function is used to convert each number to a string, and the `int` function is used to convert each character in the string back to an integer. The `sum` function is used to add up these digits. 

For example, if the input is `[10,2,56]`, the function will first sum the digits of `10` (which is `1+0=1`), then sum the digits of `2` (which is `2`), and then sum the digits of `56` (which is `5+6=11`). The function will then return `1+2+11=14`.  The unit test `assert sum_of_digits([10,2,56])==14` confirms that this is the correct output. 