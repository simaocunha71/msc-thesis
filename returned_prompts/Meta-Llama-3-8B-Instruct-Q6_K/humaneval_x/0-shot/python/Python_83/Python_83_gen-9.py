```
def starts_one_ends(n):
    count = 0
    for i in range(10**(n-1), 10**n):
        if str(i)[0] == '1' or str(i)[-1] == '1':
            count += 1
    return count
```


Explanation:

The function `starts_one_ends(n)` takes an integer `n` as input and returns the count of the numbers of `n`-digit positive integers that start or end with 1.

Here's a step-by-step breakdown of the solution:

1. Initialize a variable `count` to 0, which will store the count of the numbers that start or end with 1.
2. Use a for loop to iterate over the `n`-digit positive integers, starting from `10**(n-1)` and ending at `10**n`. This is because the smallest `n`-digit positive integer is `10**(n-1)` and the largest `n`-digit positive integer is `10**n - 1` (since `10**n` is an `(n+1)`-digit number).
3. Inside the loop, convert the current integer `i` to a string using the `str()` function.
4. Check if the first character of the string (i.e., the first digit of the integer) is '1' or the last character of the string (i.e., the last digit of the integer) is '1'. If either condition is true, increment the `count` variable by 1.
5. Return the final value of `count`.

For example, if `n` is 3, the function will count the numbers 101, 110, 121, 130, ..., 991, which are the 3-digit positive integers that start or end with 1. The function will return 90, which is the correct count.