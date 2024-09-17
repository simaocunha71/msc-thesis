```
def add_pairwise(t):
    return tuple(a + b for a, b in zip(t, t[1:]))

assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
```


The function add_pairwise takes a tuple as an argument and returns a new tuple where each element is the sum of the corresponding elements in the input tuple and the next element in the tuple. The zip function is used to iterate over the input tuple and the next element in the tuple (t[1:]). The result is a new tuple where each element is the sum of the corresponding elements in the input tuple and the next element. For example, if the input is (1, 5, 7, 8, 10), the output will be (6, 12, 15, 18). The unit test assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18) ensures that the function works correctly.