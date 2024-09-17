```
def add_pairwise(t):
    result = ()
    for i in range(1, len(t)):
        result += (t[i-1] + t[i],)
    return result
```


The function `add_pairwise` takes a tuple `t` as an input and returns a new tuple where each element is the sum of the corresponding neighboring elements in the original tuple.

The unit test `assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)` ensures that the function works correctly. It checks if the output of the function for the input `(1, 5, 7, 8, 10)` is equal to `(6, 12, 15, 18)`. If the function is implemented correctly, this test should pass.