```
def min_k(tuple_list, k):
    return sorted(tuple_list, key=lambda x: x[1])[:k]
```
This function sorts the tuple list based on the second element of each tuple (which is the value) and returns the first k elements. If there are multiple tuples with the same value, their original order is preserved because lists are not stable in Python. If you want to get the last k smallest records, you can use `sorted(tuple_list, key=lambda x: x[1])[-k:]`

The unit test `assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]` suggests that the function should return the k smallest records. So the function is implemented to sort the tuple list based on the second element of each tuple and return the first k elements. 

The time complexity of this function is O(n log n) due to the sorting operation, where n is the number of tuples in the list. The space complexity is O(n) as it needs to store the sorted list. 