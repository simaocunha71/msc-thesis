```python
def find_remainder(my_list,n):
    return pow(reduce(lambda x,y:x*y,my_list),-1,n)
```

