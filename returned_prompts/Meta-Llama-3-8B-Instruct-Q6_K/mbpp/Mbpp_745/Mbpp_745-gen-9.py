```
def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum+1):
        num_str = str(num)
        if all(int(digit) in num_str for digit in num_str):
            if all(num % int(digit) == 0 for digit in num_str):
                result.append(num)
    return result
```


This function iterates over all numbers in the given range. For each number, it checks if every digit in the number is present in the number itself (using the `all` function with a generator expression). If this condition is met, it then checks if the number is divisible by every digit in the number. If this condition is also met, the number is added to the result list. The function finally returns the list of numbers that meet the given criteria.