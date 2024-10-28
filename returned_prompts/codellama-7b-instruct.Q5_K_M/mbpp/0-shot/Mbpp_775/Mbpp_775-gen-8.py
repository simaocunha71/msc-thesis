```python
def odd_position(my_list):
    for i in range(1, len(my_list), 2):
        if my_list[i] % 2 == 0:
            return False
    return True
```
