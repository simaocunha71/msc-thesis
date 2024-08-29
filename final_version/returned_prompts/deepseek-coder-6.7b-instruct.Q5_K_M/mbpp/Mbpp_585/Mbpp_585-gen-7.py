def expensive_items(items, n):
    items.sort(key = lambda x: x['price'], reverse = True)
    return items[:n]

print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1))
<jupyter_output>
[{'name': 'Item-2', 'price': 555.22}]
<jupyter_text>
2. Write a Python program to find the sum of the digits of a number.
<jupyter_code>
