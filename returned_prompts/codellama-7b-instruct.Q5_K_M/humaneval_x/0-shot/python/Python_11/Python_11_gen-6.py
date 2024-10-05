```python
def string_xor(a: str, b: str) -> str:
    # Write your code here
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
```
