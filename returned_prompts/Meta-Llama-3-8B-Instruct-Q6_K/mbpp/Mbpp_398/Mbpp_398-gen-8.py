```
def sum_of_digits(lst):
    return sum(sum(int(digit) for digit in str(num)) for num in lst)
```


Explanation:
The function `sum_of_digits` takes a list of numbers as input. For each number in the list, it converts the number to a string, iterates over each character (digit) in the string, converts each character back to an integer, and sums up the digits. It then sums up the sums of digits for all numbers in the list. The unit test `assert sum_of_digits([10,2,56])==14` ensures the function works correctly. 







