```
def large_product(list1, list2, n):
    products = [(i, j) for i in list1 for j in list2]
    products.sort(key=lambda x: x[0]*x[1], reverse=True)
    return [i*j for i, j in products[:n]]
```





The function `large_product` takes three parameters: two lists of numbers and an integer `n`. It calculates the products of each pair of numbers, one from each list, and sorts these products in descending order. Then, it returns the `n` largest products.

The unit test `assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]` ensures that the function works correctly. It checks that the function returns the three largest products when given the lists `[1, 2, 3, 4, 5, 6]` and `[3, 6, 8, 9, 10, 6]`, and `n=3`.

This function can be used to find the `n` largest products from two lists of numbers. It is efficient because it uses a list comprehension to generate the products, and the `sort` method with a lambda function to sort the products. The `sort` method is stable, so the order of products with the same value is preserved. This ensures that the function returns the correct `n` largest products.