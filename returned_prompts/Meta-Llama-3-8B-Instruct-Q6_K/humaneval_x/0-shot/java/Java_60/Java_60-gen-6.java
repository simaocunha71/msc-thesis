        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
}

S:
The solution provided is a simple and straightforward implementation of the sum of numbers from 1 to n. It uses a for loop to iterate from 1 to n and adds each number to the sum. The function returns the sum at the end. This solution has a time complexity of O(n) as it needs to iterate through all the numbers from 1 to n. The space complexity is O(1) as it only uses a fixed amount of space to store the sum.

Example:
If you call the function sumToN(5), it will return 15 (1 + 2 + 3 + 4 + 5). If you call the function sumToN(100), it will return 5050 (1 + 2 + 3 + ... + 100). If you call the function sumToN(1), it will return 1, as there is only one number in the sum. If you call the function sumToN(10), it will return 55 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10). 

This solution is easy to understand and implement, but it may not be efficient for large values of n, as it needs to iterate through all the numbers. There are other solutions that use mathematical formulas to calculate the sum in a more efficient way. 
```python
def sumToN(n):
    return n*(n+1)//2
```
This solution has a time complexity of O(1) and a space complexity of O(1), making it more efficient for large values of n. 
```python
def sumToN(n):
    return sum(range(1, n+1))
```
This solution also has a time complexity of O(n) and a space complexity of O(1), but it is more concise and easier to understand. 
```python
def sumToN(n):
    return math.fsum(range(1, n+1))
```
This solution uses the math.fsum function to calculate the sum, which is more accurate than the sum function for large values of n. It has a time complexity of O(n) and a space complexity of O(1). 
```python
def sumToN(n):
    return sum(range(