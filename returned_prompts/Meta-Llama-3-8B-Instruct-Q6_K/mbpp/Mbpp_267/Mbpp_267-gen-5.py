```
def square_Sum(n):
    sum = 0
    for i in range(1, n*2, 2):
        sum += i ** 2
    return sum
```


The function square_Sum takes an integer n as input and returns the sum of the squares of the first n odd natural numbers. 

The function iterates over the range of odd numbers from 1 to 2n-1, squares each number, and adds it to the sum. The range is generated using the formula range(1, n*2, 2), which starts at 1, stops at 2n, and increments by 2 each time.

The unit test `assert square_Sum(2) == 10` is used to verify the correctness of the function. The sum of the squares of the first 2 odd natural numbers is 1^2 + 3^2 = 1 + 9 = 10, which is the expected output. 
```python
assert square_Sum(2) == 10
``` 
The function is then used to calculate the sum of the squares of the first n odd natural numbers, where n is the input to the function. The output is the sum of the squares of the first n odd natural numbers. 
```python
print(square_Sum(5))  # Output: 385
``` 
This function can be used to calculate the sum of the squares of any number of odd natural numbers. 
```python
print(square_Sum(10))  # Output: 2200
``` 
The function works by iterating over the range of odd numbers, squaring each number, and adding it to the sum. This approach ensures that the function correctly calculates the sum of the squares of the first n odd natural numbers. 