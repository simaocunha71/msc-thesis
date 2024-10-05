
To solve this problem, we can follow these steps:

1. Convert the integer to a string.
2. Initialize two counters, one for even and one for odd digits.
3. Loop through each character in the string. If the character is an even number (0, 2, 4, 6, or 8), increment the even counter. Otherwise, increment the odd counter.
4. Return a tuple containing the even and odd counters.

Here is the Python code that implements these steps:

```python
def even_odd_count(num):
    # Step 1: Convert integer to a string
    num_str = str(abs(num))

    # Step 2: Initialize even and odd counters
    even_counter = 0
    odd_counter = 0

    # Step 3: Loop through each character in the string
    for char in num_str:
        if int(char) % 2 == 0:  # Check if the character is an even number
            even_counter += 1
        else:
            odd_counter += 1

    # Step 4: Return a tuple containing the even and odd counters
    return (even_counter, odd_counter)
```

You can use the function like this:

```python
print(even_odd_count(12))  # Output: (1, 1)
print(even_odd_count(123))  # Output: (1, 2)
```

This function handles both positive and negative numbers. For negative numbers, it converts the number to its absolute value, as the count of even and odd digits should not depend on the sign of the number.

The time complexity of this function is O(n), where n is the number of digits in the input number. This is because we need to process each digit of the number exactly once.

The space complexity is O(1) as we are using a constant amount of extra memory to store the counters.

The function assumes that the input number is an integer and raises a `TypeError` if the input is not an integer.

```python
def even_odd_count(num):
    if not isinstance(num, int):
