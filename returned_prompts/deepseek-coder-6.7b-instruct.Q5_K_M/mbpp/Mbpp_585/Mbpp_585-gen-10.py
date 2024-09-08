def cheap_items(data,n):
    data = sorted(data, key = lambda i: i['price'])
    return data[:n]

print(cheap_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1))

"""
The function "cheap_items" takes a list of dictionaries and an integer n as input. It sorts the list of dictionaries by the 'price' key in ascending order and then returns the first n items.

In the given example, it sorts the list of items by their prices in ascending order and then returns the first item in the list.
"""
<jupyter_output>
[{'name': 'Item-1', 'price': 101.1}]
<jupyter