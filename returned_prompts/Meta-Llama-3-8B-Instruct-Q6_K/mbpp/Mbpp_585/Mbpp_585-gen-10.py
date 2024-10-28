```
def expensive_items(data, n):
    data.sort(key=lambda x: x['price'], reverse=True)
    return data[:n]
```







