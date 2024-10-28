```
def find_tuples(tuples_list, k):
    return [t for t in tuples_list if all(i % k == 0 for i in t)]
```



Explanation:
The problem is asking to write a function that takes a list of tuples and an integer k as input, and returns a list of tuples where all elements in each tuple are divisible by k.

The unit test provided, `assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]`, helps to clarify the problem by showing that the function should return all tuples from the list where all elements are divisible by the given integer k.

The solution uses a list comprehension to iterate over the input list of tuples. For each tuple, it checks if all elements are divisible by k using the `all` function and a generator expression. If all elements are divisible by k, the tuple is included in the output list. The resulting list of tuples is then returned.