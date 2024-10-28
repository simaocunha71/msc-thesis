```
def median_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    if len(numbers) % 2 == 0:
        median = (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) / 2
    else:
        median = numbers[len(numbers)//2]
    return median
```


This function first creates a list of the three input numbers and then sorts them. It then checks if the length of the list is even or odd. If it's even, it calculates the median as the average of the two middle numbers. If it's odd, it takes the middle number as the median. The function then returns the median. 

The unit test `assert median_numbers(25,55,65)==55.0` checks if the function correctly calculates the median of the numbers 25, 55, and 65, which is indeed 55.0. 
```python
print(median_numbers(25,55,65))  # Output: 55.0
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
``` 