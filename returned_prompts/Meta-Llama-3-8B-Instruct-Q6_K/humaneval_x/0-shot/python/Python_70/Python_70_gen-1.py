```
def strange_sort_list(lst):
    if not lst:
        return []
    sorted_lst = sorted(lst)
    result = []
    while sorted_lst:
        result.append(sorted_lst.pop(0))
        if sorted_lst:
            result.append(sorted_lst.pop())
    return result
```
Explanation:
The function `strange_sort_list` takes a list of integers as input and returns the list in a "strange" order. The strange order is defined as the minimum value, then the maximum of the remaining integers, then the minimum and so on.

The function first checks if the input list is empty. If it is, the function returns an empty list.

If the list is not empty, the function sorts the list in ascending order using the `sorted` function. The sorted list is then stored in the `sorted_lst` variable.

The function then initializes an empty list `result` to store the "strange" sorted list.

The function enters a while loop that continues until the `sorted_lst` list is empty. In each iteration of the loop, the function appends the smallest element of `sorted_lst` to the `result` list using `sorted_lst.pop(0)`. Then, if `sorted_lst` is not empty, the function appends the largest element of `sorted_lst` to the `result` list using `sorted_lst.pop()`.

Finally, the function returns the `result` list, which is the "strange" sorted list.