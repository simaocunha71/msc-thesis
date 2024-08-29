Here is the Python code to solve the problem:

```python
def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum + 1):
        if num < 10:
            result.append(num)
        else:
            str_num = str(num)
            if '0' in str_num:
                continue
            else:
                for digit in str_num:
                    if num % int(digit) != 0:
                        break
                else:
                    result.append(num)
    return result

print(divisible_by_digits(1,22))
```

In this code, we define a function `divisible_by_digits(startnum, endnum)`. This function takes two arguments `startnum` and `endnum`. It then iterates over all numbers from `startnum` to `endnum` inclusive. For each number, it checks whether every digit from that number is a factor of the number. If it is, the number is added to the result list. The function finally returns this list of numbers.
"""

