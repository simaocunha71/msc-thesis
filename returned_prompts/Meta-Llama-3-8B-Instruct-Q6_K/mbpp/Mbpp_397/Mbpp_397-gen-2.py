```
def median_numbers(a, b, c):
    numbers = sorted([a, b, c])
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]
```    
    This function first sorts the input numbers. Then it checks if the length of the list of numbers is even or odd. If the length is even, it calculates the median by taking the average of the two middle numbers. If the length is odd, it returns the middle number as the median. The function returns the result as a floating point number. 

    The unit test `assert median_numbers(25,55,65)==55.0` ensures that the function correctly calculates the median when the input numbers are 25, 55, and 65. The expected result is 55.0, which is the median of these numbers. 
```python
assert median_numbers(25,55,65)==55.0
```   
```python
assert median_numbers(25,55,65) == 55
```   
```python
assert median_numbers(25,65,65) == 55
```   
```python
assert median_numbers(1,2,3) == 2
```   
```python
assert median_numbers(1,3,2) == 2
```   
```python
assert median_numbers(1,1,1) == 1
```   
```python
assert median_numbers(1,2,3,4) == 2.5
```   
```python
assert median_numbers(1,2,3,4,5) == 3
```   
```python
assert median_numbers(1,2,3,4,5,6) == 3.5
```   
```python
assert median_numbers(1,2,3,4,5,6,7) == 4
```   
```python
assert median_numbers(1,2,3,4,5,6,7,8) == 4.5
```   
```python
assert median_numbers(1,2,3,4,5,6,7,8,9) == 5
```   
```python
assert median_numbers(1,2,3,4,5,6,7,8,9,10) ==