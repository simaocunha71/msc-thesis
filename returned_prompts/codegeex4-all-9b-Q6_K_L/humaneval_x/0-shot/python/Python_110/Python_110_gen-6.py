```python
def exchange(lst1, lst2):
    count = sum(x % 2 for x in lst1)
    if count == 0:
        return "YES"
    count = sum(x % 2 for x in lst2)
    if count >= count:
        return "YES"
    else:
        return "NO"

```
