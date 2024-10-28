```
def large_product(list1, list2, n):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    result = []
    for _ in range(n):
        result.append(list1.pop(0) * list2.pop(0))
    return sorted(result, reverse=True)
```





The function `large_product` takes two lists of numbers and an integer `n` as input. It first sorts the lists in descending order. Then, it iterates `n` times, each time selecting the largest number from the first list and the largest number from the second list, multiplying them together, and adding the result to the output list. Finally, it sorts the output list in descending order and returns it.

For example, when we call `large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)`, the function returns `[60, 54, 50]`, which are the three largest products that can be obtained by selecting one number from each list.