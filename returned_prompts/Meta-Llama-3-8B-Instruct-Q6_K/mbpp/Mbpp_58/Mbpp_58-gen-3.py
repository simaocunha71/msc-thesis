```
def opposite_Signs(a, b):
    return (a > 0 and b < 0) or (a < 0 and b > 0)
```  # 0 is neither positive nor negative
```python
assert opposite_Signs(1,-2) == True
```  # This test case should return True
```python
assert opposite_Signs(2,2) == False
```  # This test case should return False
```python
assert opposite_Signs(1,1) == False
```  # This test case should return False
```python
assert opposite_Signs(0,1) == True
```  # This test case should return True
```python
assert opposite_Signs(0,-1) == True
```  # This test case should return True
```python
assert opposite_Signs(1,0) == True
```  # This test case should return True
```python
assert opposite_Signs(-1,0) == True
```  # This test case should return True
```python
assert opposite_Signs(0,0) == False
```  # This test case should return False
```python
assert opposite_Signs(1,0) == True
```  # This test case should return True
```python
assert opposite_Signs(0,1) == True
```  # This test case should return True
```python
assert opposite_Signs(1,1) == False
```  # This test case should return False
```python
assert opposite_Signs(1,0) == True
```  # This test case should return True
```python
assert opposite_Signs(0,0) == False
```  # This test case should return False
```python
assert opposite_Signs(1,0) == True
```  # This test case should return True
```python
assert opposite_Signs(0,1) == True
```  # This test case should return True
```python
assert opposite_Signs(1,1) == False
```  # This test case should return False
```python
assert opposite_Signs(0,0) == False
```  # This test case should return False
```python
assert opposite_Signs(0,0) == False
```  # This test case should