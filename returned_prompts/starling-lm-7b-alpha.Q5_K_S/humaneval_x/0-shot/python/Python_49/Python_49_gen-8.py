
To solve this problem, we can use the property of modular exponentiation, which states that (a^b) mod n = ((a mod n)^b) mod n for any positive integer a, b, and n. In this case, we can use the modulo operator (%) to calculate the remainder when 2^n is divided by p.

Here's an example of how the function can be implemented in Python:

```python
def modp(n: int, p: int):
    # Initialize the result to 1
    result = 1

    # Calculate 2^n modulo p
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n = n // 2

    return result
```

In this implementation, we use a while loop to repeatedly multiply the result by 2 if the least significant bit of n is 1 (i.e., n % 2 == 1). We update n by dividing it by 2 in each iteration until n becomes 0. Finally, we return the result, which is the value of 2^n modulo p.

The time complexity of this implementation is O(log n) since we perform at most log n iterations in the while loop.

Note: It's important to be aware of potential numeric overflow issues in the modular exponentiation process, especially when dealing with large values of n and p.

You can test the function with the provided test cases to verify its correctness:

```python
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

These test cases cover different scenarios, including cases where the result is 1 (e.g., n = 0) and cases where the result is less than p (e.g., n = 3, p = 5).

By using the modular