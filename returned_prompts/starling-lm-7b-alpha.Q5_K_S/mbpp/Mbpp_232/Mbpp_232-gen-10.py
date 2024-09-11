```
def larg_nnum(input_list,num):
    sorted_list=sorted(input_list,reverse=True)
    return sorted_list[:num]
```

Explanation:
The function `larg_nnum` takes in a list and an integer `n` as parameters. It first sorts the input list in descending order using the `sorted` function with the `reverse=True` argument. Then it returns a new list containing the first `n` elements of the sorted list using list slicing. This new list will contain the `n` largest items from the input list.

In the provided example, the function `larg_nnum` is called with the list `[10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]` and the integer `2`. The function will sort the list in descending order to get `[100, 90, 70, 50, 50, 40, 20, 20, 60, 80, 10]`. Then it will return a new list containing the first two elements of the sorted list, which are `[100, 90]`. The `assert` statement checks if the returned list is equal to the set of `[100, 90]` and passes the test as expected.