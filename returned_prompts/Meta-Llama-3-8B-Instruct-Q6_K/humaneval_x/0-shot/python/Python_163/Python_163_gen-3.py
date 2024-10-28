```
def generate_integers(a, b):
    if a > b:
        a, b = b, a
    return [i for i in range(a, b+1) if i % 2 == 0]
```
Explanation:

*   We first check if `a` is greater than `b`. If it is, we swap their values to ensure `a` is the smaller number and `b` is the larger number.
*   We use a list comprehension to generate the list of even integers between `a` and `b`. The condition `i % 2 == 0` filters out odd numbers, leaving only the even digits.
*   The `range` function generates a sequence of numbers from `a` to `b` (inclusive), which we then iterate over to build the list of even integers.
*   The resulting list is returned by the function. If `a` and `b` are equal, the function returns an empty list, as there are no even digits between them. If `a` is greater than `b`, the function returns an empty list, as there are no even digits between `b` and `a`. If `a` and `b` are equal, the function returns a list containing only `a`. If `a` is greater than `b`, the function returns an empty list. Otherwise, the function returns a list of even integers between `a` and `b`.