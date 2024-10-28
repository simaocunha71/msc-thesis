```python
def check(num):
    num_str = str(num)
    if num_str[::-1] == num_str[1:]:
        return True
    return False
```
