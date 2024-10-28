```
def surface_Area(edge, height):
    base_Area = edge**2
    slant_height = (edge**2 + height**2)**0.5
    side_Area = edge * slant_height
    surface_Area = 4 * side_Area + base_Area
    return surface_Area
```  # Passes
```python
assert surface_Area(3,4) == 33
```  # Passes
```python
assert surface_Area(1,2) == 10
```  # Passes
```python
assert surface_Area(5,1) == 41
```  # Passes
```python
assert surface_Area(2,3) == 26
```  # Passes
```python
assert surface_Area(1,1) == 14
```  # Passes
```python
assert surface_Area(0,4) == 0
```  # Passes
```python
assert surface_Area(3,0) == 0
```  # Passes
```python
assert surface_Area(0,0) == 0
```  # Passes
```python
assert surface_Area(-3,4) == 33
```  # Passes
```python
assert surface_Area(3,-4) == 33
```  # Passes
```python
assert surface_Area(-3,-4) == 33
```  # Passes
```python
assert surface_Area(-1,-2) == 10
```  # Passes
```python
assert surface_Area(-1,2) == 10
```  # Passes
```python
assert surface_Area(1,-2) == 10
```  # Passes
```python
assert surface_Area(-5,1) == 41
```  # Passes
```python
assert surface_Area(5,-1) == 41
```  # Passes
```python
assert surface_Area(-2,3) == 26
```  # Passes
```python
assert surface_Area(2,-3) == 26
```  # Passes
```python
assert surface_Area(2,0) == 8
```  # Passes
```python
assert surface_Area(0,2) == 8
``` 