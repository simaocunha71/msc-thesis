def large_product(list1, list2, num):
    products = []
    for i in list1:
        for j in list2:
            products.append(i*j)
    products.sort(reverse=True)
    return products[:num]

print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3))

"""
This function works by creating a list of products by multiplying each element of list1 with each element of list2.
Then it sorts the list of products in descending order.
Finally, it returns the first 'num' elements of the sorted list of products.
"""
<jupyter_output>
[60, 54, 50]
<jupyter_text>
Question 2
<jupyter_code>
