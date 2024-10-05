Here is a Python function that efficiently computes the n-th element of the fib4 number sequence without using recursion:
```
def fib4(n: int):
    if n <= 1:
        return 0
    if n == 2:
        return 2
    fib4_values = [0, 0, 2, 0]
    for i in range(4, n + 1):
        fib4_values.append(fib4_values[i-1] + fib4_values[i-2] + fib4_values[i-3] + fib4_values[i-4])
    return fib4_values[n]
```
The function first checks for the base cases (n <= 1 and n == 2). Then it initializes a list `fib4_values` to store the fib4 numbers. The list is initialized with the base cases. Then it iterates from 4 to n and calculates the fib4 number for each i by adding the previous four fib4 numbers. Finally, it returns the n-th element of the list.

You can test the function with the given test cases:
```
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
This function has a time complexity of O(n) because it iterates from 4 to n to calculate the fib4 number. It has a space complexity of O(n) because it stores the fib4 numbers in a list of length n. This is an efficient solution because it avoids the overhead of recursive function calls.