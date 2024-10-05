```
def count_nums(arr):
    return sum(1 for x in arr if sum(int(digit) for digit in str(abs(x))) > 0)
```


This function works by iterating over each number in the array. For each number, it calculates the sum of its digits (ignoring the sign of the number, by taking the absolute value). It then checks if this sum is greater than 0. If it is, it counts this as a "positive" number. The function returns the total count of these "positive" numbers. The `str(abs(x))` converts the number to a string, which allows us to iterate over its digits. The `int(digit) for digit in ...` converts each character in the string back to an integer, and the `sum(...)` adds them all up. The `for x in arr if ...` is a generator expression that iterates over the array, and only includes the numbers for which the sum of their digits is greater than 0. The `sum(...)` at the beginning of the function counts up how many of these "positive" numbers there are.