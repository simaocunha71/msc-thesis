from itertools import combinations


def find_combinations(tuple_list):
    # flatten the list of tuples
    flat_list = [item for sublist in tuple_list for item in sublist]
    # get the combinations of sums
    combs = list(combinations(flat_list, 2))
    # convert the combinations of tuples back to tuples
    return [(sum(tup1), sum(tup2)) for tup1, tup2 in combs]


assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# The time complexity of the function is O(n^2) because it first flattens the list of tuples which takes O(n) time. Then it gets the combinations of sums which takes O(n^2) time. The space complexity of the function is O(1) because it only uses a constant amount of extra space.

# Python3 program to find all unique
# combinations of two elements from
# the list. 

# Python3 program to find all unique
# combinations of two elements from
# the list. 

# Function to print all combinations
# of two elements from the list. 

# Function to print all combinations
# of two elements from the list. 


def print_combinations(arr, n):
    # Iterate through list and find all 
    # combinations of two elements 
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            print(arr[i], arr[j], sep=",")


# Driver program 
arr = [1, 2, 3, 4]
n = len(arr)
print_combinations(arr, n)
```
python

```python
from itertools import combinations