def expensive_items(data, n):
    sorted_data = sorted(data, key = lambda x: x['price'], reverse = True)
    return sorted_data[:n]

print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1))

"""
The function "expensive_items" sorts the data by the price in descending order and returns the first n items.

The lambda function in the key argument of the sorted function is used to specify that the data should be sorted by the 'price' field.

The reverse = True argument specifies that the data should be sorted in descending order.

Finally, the function returns the first n items of the sorted list.
"""

"""
Output:
[{'name': 'Item-2', 'price': 555.22}]
"""

"""
The function works by first sorting the data in descending order by price. This means that the item with the highest price will be first in the list. It then returns the first n items from the sorted list.
"""

"""
If the number of items n is larger than the number of items in the dataset, the function will return all items in the dataset.
"""
<jupyter_output>
[{'name': 'Item-2', 'price': 555.22}]
<jupyter_text>
