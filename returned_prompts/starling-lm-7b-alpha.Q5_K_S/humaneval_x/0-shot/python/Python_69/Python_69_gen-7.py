
def search(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    max_val = -1
    for i in freq:
        if freq[i] >= i:
            if i > max_val:
                max_val = i
    return max_val


# print(search([4, 1, 2, 2, 3, 1]))
# print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
# print(search([5, 5, 4, 4, 4]))





# In[ ]:

```

```python
```