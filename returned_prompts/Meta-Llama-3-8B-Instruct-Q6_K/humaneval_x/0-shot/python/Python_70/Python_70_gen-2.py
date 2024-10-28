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
    # test cases
    print(strange_sort_list([1, 2, 3, 4]))  # [1, 4, 2, 3]
    print(strange_sort_list([5, 5, 5, 5]))  # [5, 5, 5, 5]
    print(strange_sort_list([]))  # []



# Explanation:
The problem is asking to sort a list of integers in a specific way. The sort order is: start with the smallest number, then the largest number, then the smallest number again, and so on. If the list has an even number of elements, the last element should be the largest.

Here is the solution:
```python
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
The idea is to first sort the list, then iterate over it in a specific way. We start by adding the smallest number to the result, then the largest number, then the smallest number again, and so on. If the list has an even number of elements, the last element should be the largest.

Here are some test cases:
```python
print(strange_sort_list([1, 2, 3, 4]))  # [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # [5, 5, 5, 5]
print(strange_sort_list([]))  # []
```
The function works correctly for these test cases. If you run the function with a list of integers, it will return the list in the strange sort order. If the list is empty, it will return an empty list.