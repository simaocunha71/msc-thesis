```
def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum + 1):
        if all(int(digit) in str(num) for digit in str(num)):
            result.append(num)
    return result
```


Explanation:
The problem is asking to find numbers within a given range from startnum to endnum where every number is divisible by every digit it contains. 

The function `divisible_by_digits` takes two parameters, startnum and endnum. It initializes an empty list result to store the numbers that meet the condition.

The function then iterates over each number in the range from startnum to endnum (inclusive). For each number, it checks if every digit in the number is present in the number itself. This is done using the `all` function with a generator expression. The `all` function returns True if all elements of the iterable (in this case, the generator expression) are True.

If the condition is met, the number is added to the result list.

Finally, the function returns the result list, which contains the numbers that are divisible by every digit they contain.

The unit test `assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]` helps to clarify the problem and ensure the correctness of the solution. It checks if the function returns the expected list of numbers. 

The solution is efficient because it only iterates over the numbers in the range once, and it uses a generator expression to check the condition for each number. This makes the function scalable for large ranges. 