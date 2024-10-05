
def fizz_buzz(n: int):
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            if '7' in str(i):
                count += 1
    return count



# Made By Mostafa_Khaled
```

    def fizz_buzz(n: int):
        count = 0
        for i in range(n):
            if i % 11 == 0 or i % 13 == 0:
                if '7' in str(i):
                    count += 1
        return count
# Made By Mostafa_Khaled
```

    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3

```

    The above code defines a function called `fizz_buzz` that takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The function uses a for loop to iterate over all integers from 0 to `n-1`. For each integer, it checks if it is divisible by 11 or 13 using the modulo operator (`%`). If the integer is divisible by either 11 or 13, it then checks if the digit 7 appears in the integer by converting the integer to a string and checking if the string contains the digit 7. If the digit 7 is found, the count variable is incremented by 1. Finally, the function returns the count variable, which represents the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13.

```

The above code demonstrates the usage of the `fizz_buzz` function with different inputs and prints the expected output for each input. The function is called with the input values 50, 78, and 79, and the returned values are printed to the console. The expected output for each input is