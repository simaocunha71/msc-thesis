    # Your code here
    lst = lst[:]
    sorted_lst = []
    while lst:
        min_num = min(lst)
        sorted_lst.append(min_num)
        lst.remove(min_num)
        if len(lst) == 0:
            break
        max_num = max(lst)
        sorted_lst.append(max_num)
        lst.remove(max_num)
    return sorted_lst











# Code above this line can be used as is, and is tested.
# Code below this line is incomplete or unverified and may require fixing, and will not be tested until fixed.

# Below is some sample usage of your function to help you check if it's working.
if __name__ == '__main__':
    print(strange_sort_list([1, 2, 3, 4]))  # Expected: [1, 4, 2, 3]
    print(strange_sort_list([5, 5, 5, 5]))  # Expected: [5, 5, 5, 5]
    print(strange_sort_list([]))  # Expected: []
    print(strange_sort_list([10, 100, 1000, 10000]))  # Expected: [10, 10000, 1000, 100]
```
