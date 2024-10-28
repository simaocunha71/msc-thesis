```
def sort_numeric_strings(lst):
    return sorted(map(int, lst))
```
The function `sort_numeric_strings` takes a list of strings as input. It uses the built-in `map` function to convert each string in the list to an integer, and then uses the built-in `sorted` function to sort the list of integers in ascending order. The result is a new list that contains the same strings but in sorted order. 

For example, the input `['4','12','45','7','0','100','200','-12','-500']` will be converted to `[-500, -12, 0, 4, 7, 12, 45, 100, 200]`. 

The unit test `assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]` ensures that the function works correctly.  The test checks that the function returns the correct sorted list for the given input. 
```
python
assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
```  ```python
print(sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500']))
```

The output will be: 
`[-500, -12, 0, 4, 7, 12, 45, 100, 200]` 
```
```python
def sort_numeric_strings(lst):
    return sorted(map(int, lst))
print(sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500']))
```

The output will be: 
`[-500, -12, 0, 4, 7, 12, 45, 100, 200]` 
```python
print(sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500']))
```

The output will be: 
`[-500, -12, 0, 4, 7, 12, 45, 100, 200]` 
```
```python
def sort_numeric_strings(lst):
