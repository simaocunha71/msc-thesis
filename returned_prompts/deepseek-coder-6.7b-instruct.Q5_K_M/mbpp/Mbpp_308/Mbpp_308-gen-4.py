
def large_product(list1, list2, n):
    products = []
    for i in list1:
        for j in list2:
            products.append(i*j)
    products.sort(reverse=True)
    return products[:n]

print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3))

"""
This program works by iterating over each element in both lists and calculating their product. This is done for every pair of elements in both lists. The results are stored in a list named 'products'. This list is then sorted in descending order. Finally, the function returns the first 'n' elements of the sorted list, which are the 'n' largest products.
"""

assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]

"""
This assert statement tests if the function large_product is working correctly. If the function returns the expected output, the assert statement will not raise an AssertionError. If the function returns a different output, the assert statement will raise an AssertionError.
"""
<jupyter_output>
[60, 54, 50]
<jupyter_text>
Problem 5
<jupyter_code>
