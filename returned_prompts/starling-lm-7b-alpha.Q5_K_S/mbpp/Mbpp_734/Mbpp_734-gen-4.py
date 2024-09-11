Here's a solution:

```python
def sum_Of_Subarray_Prod(lst):
    l = len(lst)
    if l == 0:
        return 0
    if l == 1:
        return lst[0]
    if l == 2:
        return lst[0]*lst[1] + lst[1]*lst[0]
    return sum([lst[i]*lst[j]*lst[k] for i in range(l) for j in range(i+1,l) for k in range(j+1,l)])
```

Explanation:

The function `sum_Of_Subarray_Prod` takes a list `lst` as input. It first checks if the length of the list is 0. If it is, it returns 0 as there are no elements to calculate the sum of products of sublists for.

Next, it checks if the length of the list is 1. If it is, it returns the only element in the list as the sum of products of sublists is the same as the sum of products of all elements in the list.

Finally, if the length of the list is 2, it calculates the sum of products of sublists by multiplying each element with the other and summing the result. This is because there are only two elements in the list and the sublists are formed by taking one element at a time.

For lists with length greater than 2, it uses list comprehension to generate all possible sublists by taking each element at a time. It then multiplies each sublist with the other sublists and sums the result to get the total sum of products of all sublists.

The function returns this total sum as the result.

The assert statement at the beginning of the code is used to test the function with a sample input `[1,2,3]` and verify if the expected output is 20. This helps in validating the correctness of the function.

Overall, the function `sum_Of_Subarray_Prod` calculates the sum of products of all possible sublists of a given list in Python.

```python
assert sum_Of_Subarray_Prod([1,2,3]) == 20
