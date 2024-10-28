```
def pluck(arr):
    even_nodes = [node for node in arr if node % 2 == 0]
    if not even_nodes:
        return []
    return [min(even_nodes), arr.index(min(even_nodes))]
```


Explanation:
The function `pluck` takes an array `arr` as input, and returns a list containing the smallest even value and its index in the original array.

1. First, we filter the array to get a list of all even nodes using a list comprehension.
2. If the list of even nodes is empty, we return an empty list.
3. Otherwise, we find the smallest even value in the list using the `min` function.
4. We find the index of the smallest even value in the original array using the `index` method.
5. We return a list containing the smallest even value and its index.

Example 1:
Input: [4,2,3]
Output: [2, 1]
Explanation: 2 has the smallest even value, and 2 has the smallest index.

Example 2:
Input: [1,2,3]
Output: [2, 1]
Explanation: 2 has the smallest even value, and 2 has the smallest index.

Example 3:
Input: []
Output: []
Explanation: The input array is empty, so we return an empty list.

Example 4:
Input: [5, 0, 3, 0, 4, 2]
Output: [0, 1]
Explanation: 0 is the smallest value, but there are two zeros, so we choose the first zero, which has the smallest index.