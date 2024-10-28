    def fibfib(n: int):
        if n <= 1:
            return 0
        if n == 2:
            return 1
        a, b, c = 0, 0, 1
        for _ in range(3, n+1):
            a, b, c = b, c, a+b+c
        return c

    print(fibfib(1))  # 0
    print(fibfib(5))  # 4
    print(fibfib(8))  # 24

Explanation:
The function `fibfib` calculates the nth element of the fibfib sequence. It uses a for loop to iterate from 3 to n, updating the variables `a`, `b`, and `c` to the next values in the sequence. The base cases are handled separately. The function returns the value of `c` which is the nth element of the sequence. The time complexity is O(n) as we are doing a constant amount of work for each iteration of the loop. The space complexity is O(1) as we are using a constant amount of space to store the variables `a`, `b`, and `c`. 





```python
def fibfib(n: int):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    a, b, c = 0, 0, 1
    for _ in range(3, n+1):
        a, b, c = b, c, a+b+c
    return c

print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```





```python
def fibfib(n: int):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    a, b, c = 0, 0, 1
    for _ in range(3, n+1):
        a, b, c = b, c, a+b+c
    return c

print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```





```python
def fibfib(n: int):
    if n <= 1:
        return 0
   