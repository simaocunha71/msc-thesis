```
def sum_of_digits(lst):
    return sum(sum(int(digit) for digit in str(num)) for num in lst)
```


This function works by iterating over each number in the input list, converting the number to a string, and then summing the digits of the string. The `sum` function is used with a generator expression to calculate the sum of the digits, and then the `sum` function is used again with a generator expression to calculate the total sum of the sums of the digits. The unit test `assert sum_of_digits([10,2,56])==14` demonstrates the expected behavior of the function.