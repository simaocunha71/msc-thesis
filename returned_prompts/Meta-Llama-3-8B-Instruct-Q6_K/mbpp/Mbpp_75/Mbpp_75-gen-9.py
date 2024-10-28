```
def find_tuples(tuples, k):
    return [t for t in tuples if all(i % k == 0 for i in t)]
```
This function uses a list comprehension to iterate over each tuple in the input list. For each tuple, it checks if all elements are divisible by k using the `all` function and a generator expression. If all elements are divisible by k, the tuple is included in the output list. If not, it is skipped. The function returns a list of tuples that have all elements divisible by k. 
For example, if we call `find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6)`, it will return `[(6, 24, 12)]` because only this tuple has all elements divisible by 6. 