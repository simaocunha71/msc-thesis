
This function works by iterating over all n-digit positive integers, converting each integer to a string, and checking if the string starts or ends with '1'. If it does, it increments the count.

Here's a more efficient solution using Python's string formatting and list comprehensions:

```
def starts_one_ends(n):
    return len([str(i) for i in range(10**(n-1), 10**n) if str(i).startswith('1') or str(i).endswith('1')])
```

This function does the same thing as the previous one, but it does it in a more concise and efficient way. It uses a list comprehension to generate a list of strings that start or end with '1', and then returns the length of that list. This is more efficient because it avoids the need to increment a counter variable.