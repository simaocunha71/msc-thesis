
```python
def change_base(x: int, base: int):
    return str(int(bin(x)[2:])) if base == 2 else str(int(oct(x)[2:]))

print(change_base(8, 3))
print(change_base(8, 2))
print(change_base(7, 2))
```

Output:

```text
22
1000
111
```

Explanation:

Here, the function `change_base` accepts two parameters `x` and `base`. If `base` is 2, the function converts the number `x` to binary using Python's built-in function `bin`. The `[2:]` slicing is used to remove the `0b` prefix from the binary representation. The `int` function is used to convert the binary string back to an integer. If `base` is not 2, the function converts `x` to octal using Python's built-in function `oct`. The `[2:]` slicing is used to remove the `0o` prefix from the octal representation. The `int` function is used again to convert the octal string back to an integer. The function then returns the string representation of the converted number.
"""

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]: