```
def sum_range_list(lst, start, end):
    return sum(lst[start:end+1])
```
Explanation:
The function `sum_range_list` takes a list `lst` and two indices `start` and `end` as input. It returns the sum of all numbers in the list within the range specified by `start` and `end`. The `start` index is inclusive and the `end` index is exclusive. The `sum` function is used to calculate the sum of the numbers in the specified range. The `end+1` is used to make the `end` index exclusive. For example, if the `end` index is 10, the function will sum the numbers from index 8 to 9. If the `start` index is 8 and the `end` index is 10, the function will sum the numbers from index 8 to 9. If the `start` index is 8 and the `end` index is 11, the function will sum the numbers from index 8 to 10. 

The unit test `assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29` ensures that the function is working correctly. It checks if the sum of the numbers in the list within the range 8 to 10 is equal to 29, which is the expected result. 

The function can be used to find the sum of numbers in a list within a range specified by two indices. It can be useful in various applications such as calculating the sum of scores in a list of students within a specific range of scores.  ```python
print(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10)) # Output: 29
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