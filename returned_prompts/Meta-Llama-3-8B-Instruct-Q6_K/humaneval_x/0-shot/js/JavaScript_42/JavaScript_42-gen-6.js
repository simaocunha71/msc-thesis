Here is a simple Python solution using list comprehension:

```python
def incrList(l):
    return [i+1 for i in l]
```

For example, `incrList([1, 2, 3])` would return `[2, 3, 4]`. This function takes a list `l` as input, and returns a new list where each element is incremented by 1. The `i+1 for i in l` part is a list comprehension that iterates over each element `i` in the input list `l`, and adds 1 to it. The resulting list of incremented values is then returned. This function is concise, efficient, and easy to read and understand.