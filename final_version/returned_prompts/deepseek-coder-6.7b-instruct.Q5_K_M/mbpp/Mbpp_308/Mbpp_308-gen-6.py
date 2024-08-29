Here is the Python function for the problem:

```python
def large_product(list1, list2, n):
    products = []
    for i in list1:
        for j in list2:
            products.append(i*j)
    products.sort(reverse=True)
    return products[:n]
```

This function first finds all possible products of one factor from each list, sorts them in descending order, and returns the first `n` products.

Let's test this function with the provided example:

```python
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3))
# Output: [60, 54, 50]
```

This function works by iterating over each factor in the first list, then iterating over each factor in the second list. For each pair of factors, it calculates the product and adds it to the list of products. Once all possible products have been calculated, it sorts the list in descending order and returns the first `n` products.

Please note that the time complexity of this function is O(n^2), where n is the size of one of the lists. This is due to the fact that the function iterates over each factor in one list for each factor in the other list. This could be improved by using a more efficient data structure or algorithm to find the n largest products.

This function assumes that the lists contain integers and the number n is positive. If this is not the case, you may need to add error checking to handle these cases.

Also, please note that the function returns a list of products, not a list of pairs of factors. If you want to return a list of pairs of factors, you would need to modify the function accordingly.

Lastly, this function uses the sort function with reverse=True to sort the list in descending order. This means that the largest product is first, and the smallest product is last. If you want to sort the list in ascending order, you would need to change reverse=True to reverse=False.

Hope this helps, and let me know if you have any other questions.
"""

