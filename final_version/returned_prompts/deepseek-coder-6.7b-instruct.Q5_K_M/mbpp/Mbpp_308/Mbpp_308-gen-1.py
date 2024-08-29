def large_product(list1, list2, n):
    products = []
    for i in list1:
        for j in list2:
            products.append(i*j)
    products.sort(reverse=True)
    return products[:n]

print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3))

# Output: [60, 54, 50]

"""
Here, we first create a list of products by iterating over every pair of elements from both lists. Then, we sort this list in descending order and return the first n elements.
"""

# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Where, n is the length of the input lists.

# This solution assumes that the input lists do not contain any non-numeric elements.
# If that's not the case, you should add error handling code to deal with such inputs.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
