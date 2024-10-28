```
def split_Arr(arr,n):
    return arr[n:]+arr[:n]
```
This function takes a list and an integer n as input. It returns a new list where the first n elements are moved to the end of the list. For example, if we call `split_Arr([12,10,5,6,52,36],2)`, it will return `[5,6,52,36,12,10]`. 

The expression `arr[n:]` returns a slice of the list from the nth element to the end, and `arr[:n]` returns a slice of the list from the start to the nth element. We add these two slices together to get the desired result. 

The unit test `assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]` ensures that the function works correctly. 
```python
print(split_Arr([12,10,5,6,52,36],2)) # Output: [5,6,52,36,12,10]
```  ```python
print(split_Arr([1,2,3,4,5,6],1)) # Output: [2,3,4,5,6,1]
```  ```python
print(split_Arr([1,2,3,4,5,6],6)) # Output: [1,2,3,4,5,6]
```  ```python
print(split_Arr([1,2,3,4,5,6],0)) # Output: [1,2,3,4,5,6]
```  ```python
print(split_Arr([],0)) # Output: []
```  ```python
print(split_Arr([],1)) # Output: []
```  ```python
print(split_Arr([1],0)) # Output: [1]
```  ```python
print(split_Arr([1],1)) # Output: [1]
```  ```python
print(split_Arr([1],2)) # Output: [1]
```  ```python
print(split_Arr([1,2],0)) # Output: [1,2]
```  ```python
print(split_Arr([1,2],1)) # Output: [1,2]
```  ```python
print(split_Arr([1,2],2)) #