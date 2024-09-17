```
def large_product(list1, list2, k):
    products = [(a, b, a*b) for a in list1 for b in list2]
    products.sort(key=lambda x: x[2], reverse=True)
    return [x[2] for x in products[:k]]
```
In this problem, we are asked to find the specified number of largest products from two given lists, selecting one factor from each list.

The given unit test `assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]` helps to understand the problem better. It indicates that we need to find the 3 largest products from the two given lists.

We can solve this problem by generating all possible products of elements from the two lists, sorting them in descending order, and then returning the specified number of largest products.

Here is the Python solution:
```
def large_product(list1, list2, k):
    products = [(a, b, a*b) for a in list1 for b in list2]
    products.sort(key=lambda x: x[2], reverse=True)
    return [x[2] for x in products[:k]]
```
This function works as follows:
- It generates a list of tuples, where each tuple contains two elements from the input lists and their product.
- It sorts this list of tuples in descending order based on the product.
- It returns a list of the specified number of largest products. The `products[:k]` expression returns the first `k` elements of the sorted list, which are the `k` largest products. The `x[2] for x in products[:k]` expression extracts the products from these tuples and returns them as a list. 