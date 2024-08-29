```python
def add_string(lst, st):
    return [st.format(i) for i in lst]

print(add_string([1,2,3,4],'temp{0}'))
```

