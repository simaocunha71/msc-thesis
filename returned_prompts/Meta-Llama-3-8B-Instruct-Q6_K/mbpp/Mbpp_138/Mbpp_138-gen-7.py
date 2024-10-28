```
def is_Sum_Of_Powers_Of_Two(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    for i in range(2**31).__reversed__():
        if 2**i <= n:
            if is_Sum_Of_Powers_Of_Two(n-2**i):
                return True
    return False
```


Note: This solution is not efficient for large numbers as it involves a lot of repeated calculations. It is also not efficient in terms of space complexity as it uses recursion and function calls. It is also not efficient in terms of time complexity as it has a time complexity of O(2^n) which is not efficient for large numbers. For large numbers, you would need a more efficient algorithm that uses bitwise operations and does not involve recursion or function calls. Here is a more efficient solution using bitwise operations and without recursion or function calls:
```
def is_Sum_Of_Powers_Of_Two(n):
    if n <= 0:
        return False
    while n > 0:
        if n & 1:
            return False
        n = n >> 1
    return True
```
This solution has a time complexity of O(log n) and a space complexity of O(1), making it more efficient for large numbers. It works by repeatedly checking if the least significant bit of the number is 1. If it is, it returns False. If not, it shifts the number to the right and repeats the process. If the number becomes 0, it returns True. This solution is more efficient and scalable than the previous one.