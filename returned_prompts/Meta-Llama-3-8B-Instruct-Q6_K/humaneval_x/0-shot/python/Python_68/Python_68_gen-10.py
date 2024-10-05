```
def pluck(arr):
    even_nodes = [i for i, x in enumerate(arr) if x % 2 == 0]
    if not even_nodes:
        return []
    smallest_even_value = min(arr[i] for i in even_nodes)
    smallest_even_index = even_nodes[even_nodes.index(min(even_nodes, key=lambda x: arr[x]))]
    return [smallest_even_value, smallest_even_index]
```


Explanation:

*   First, we create a list `even_nodes` of indices where the value at that index is even.
*   If `even_nodes` is empty, it means there are no even values in the array, so we return an empty list.
*   We find the smallest even value by iterating over `even_nodes` and finding the minimum value.
*   We then find the index of the smallest even value by iterating over `even_nodes` again and finding the index of the smallest even value.
*   We return a list containing the smallest even value and its index.

This solution has a time complexity of O(n) because we iterate over the array twice, where n is the length of the array. The space complexity is O(n) because we store the indices of the even nodes in a list.