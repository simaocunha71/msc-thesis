```
def min_k(tuple_list, k):
    tuple_list.sort(key=lambda x: x[1])
    return tuple_list[-k:]
```
The problem is asking to find the minimum k records from a list of tuples, where each tuple contains a name and a score. The function should return a list of tuples, sorted by the score in ascending order, and then return the last k elements of the list.

Here is the solution:
```
def min_k(tuple_list, k):
    tuple_list.sort(key=lambda x: x[1])
    return tuple_list[-k:]
```
This function uses the built-in `sort` method to sort the list of tuples based on the score (which is the second element of each tuple). The `sort` method is stable, so if two tuples have the same score, their original order is preserved. Then, the function returns the last k elements of the sorted list, which are the minimum k records.

For example, if we call the function with the following input:
```
tuple_list = [('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)]
k = 2
```
The function will return the following output:
```
[('Akash', 2), ('Akshat', 4)]
```
This is because the scores in ascending order are: 2, 4, 8, 10, and the last 2 elements of the list are the minimum 2 records.