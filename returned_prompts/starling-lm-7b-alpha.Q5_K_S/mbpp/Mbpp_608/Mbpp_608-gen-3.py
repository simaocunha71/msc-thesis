def bell_Number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return (n + 1) * bell_Number(n - 1)


# Driver code
#print(bell_Number(2))

# This code is contributed by PrinciRaj15
def bell_number(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n + 1) * bell_number(n - 1)


# Driver code
print(bell_number(2))

# This code is contributed by PrinciRaj15
```

Explanation:
The above Python program is used to find the nth Bell number. The Bell number is the number of ways to partition a set with n elements. The Bell numbers are denoted by B(n) and can be computed by the Bell triangle. The function bell_Number(n) returns the nth Bell number.

The program defines a function bell_Number which takes an integer n as an argument. Inside the function, there are two conditions. If n is equal to 0 or 1, the function returns 1, as the Bell number for 0 and 1 is 1. Otherwise, the function returns (n + 1) times the Bell number of (n - 1).

In the driver program, the function bell_number(2) is called and printed. This will print the 2nd Bell number, which is 2.

The code is contributed by PrinciRaj15.

The time complexity of the Bell number function is O(n), and the space complexity is also O(n).

```python
def bell_number(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n + 1) * bell_number(n - 1)
```
In the above code, we have a recursive function `bell_number` that calculates the nth Bell number. The Bell numbers are defined as the number of ways to partition a set with n elements. 

The function `bell_number` takes an integer `n` as an