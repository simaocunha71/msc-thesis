def large_product(lst1, lst2, n):
    products = []
    for i in lst1:
        for j in lst2:
            products.append(i*j)
    products.sort(reverse=True)
    return products[:n]

print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3))

"""
Here, we are calculating the product of each element in lst1 with every element in lst2 and storing all these products in a list. 
We are sorting this list in descending order and then slicing the first n elements from this list. These are the n largest products.
"""
<jupyter_output>
[60, 54, 50]
<jupyter_text>
Problem 3:
<jupyter_code>
