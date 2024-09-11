def sum_digits(x):
    s = 0
    while(x!=0):
        s+=x%10
        x//=10
    return s


# Another approach
def sum_digits(x):
    return sum(map(int,str(x)))



```
```
def sum_digits(x):
    s = 0
    while(x!=0):
        s+=x%10
        x//=10
    return s
```
```python
def sum_digits(x):
    return sum(map(int,str(x)))
```