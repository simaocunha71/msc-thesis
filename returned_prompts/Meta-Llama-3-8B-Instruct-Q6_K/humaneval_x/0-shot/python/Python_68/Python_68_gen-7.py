```
def pluck(arr):
    even_nodes = [(n, i) for i, n in enumerate(arr) if n % 2 == 0]
    if not even_nodes:
        return []
    return [min(node[0] for node in even_nodes), even_nodes[0][1]]
```  Python 3.6.8

The given problem can be solved using list comprehension and the built-in functions `enumerate` and `min`.

Here's the code:

```
def pluck(arr):
    even_nodes = [(n, i) for i, n in enumerate(arr) if n % 2 == 0]
    if not even_nodes:
        return []
    return [min(node[0] for node in even_nodes), even_nodes[0][1]]
```

Explanation:

1. The list comprehension `(n, i) for i, n in enumerate(arr) if n % 2 == 0` creates a list of tuples, where each tuple contains a node value and its index. The `enumerate` function returns a tuple containing a count (from the start which defaults to 0) and the values obtained from iterating over the sequence (`arr`). The `if n % 2 == 0` condition filters the nodes to only include even values.

2. If the `even_nodes` list is empty (i.e., there are no even values in the array), the function returns an empty list `[]`.

3. Otherwise, the function returns a list containing the smallest even value and its index. The `min` function is used to find the smallest even value, and the index of the first occurrence of this value is obtained using `even_nodes[0][1]`.  Python 3.6.8

```
def pluck(arr):
    even_nodes = [(n, i) for i, n in enumerate(arr) if n % 2 == 0]
    if not even_nodes:
        return []
    return [min(node[0] for node in even_nodes), even_nodes[0][1]]
```  Python 3.6.8

The given problem can be solved using list comprehension and the built-in functions `enumerate` and `min`.

Here's the code:

```
def pluck(arr):
    even_nodes = [(n, i) for i, n in enumerate(arr) if n % 2 == 0]
    if not even_nodes:
        return []
    return [min(node[0] for node in