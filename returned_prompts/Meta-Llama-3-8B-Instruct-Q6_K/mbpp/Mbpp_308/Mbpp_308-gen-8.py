```
def large_product(list1, list2, k):
    products = [(i, j) for i in list1 for j in list2]
    products.sort(key=lambda x: x[0]*x[1], reverse=True)
    return [x[0]*x[1] for x in products[:k]]
```


The function `large_product` takes three parameters: two lists of numbers and an integer `k`. It generates all possible products of a number from the first list and a number from the second list. It then sorts these products in descending order and returns the `k` largest products.

The unit test `assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]` checks that the function returns the three largest products when given the lists `[1, 2, 3, 4, 5, 6]` and `[3, 6, 8, 9, 10, 6]`, and the number `3`. The expected output is `[60, 54, 50]`, which are the three largest products. 







