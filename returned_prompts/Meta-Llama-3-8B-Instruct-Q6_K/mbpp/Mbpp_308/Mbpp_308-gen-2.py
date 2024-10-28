```
def large_product(list1, list2, n):
    products = [(a, b, a*b) for a in list1 for b in list2]
    products.sort(key=lambda x: x[2], reverse=True)
    return [x[2] for x in products[:n]]
```
This function first generates all possible products of elements from the two lists. Then it sorts these products in descending order. Finally, it returns the specified number of largest products. The unit test `assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]` helps to clarify the problem and ensures the correctness of the solution. 





