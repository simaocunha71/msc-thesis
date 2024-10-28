```
def min_k(records, k):
    sorted_records = sorted(records, key=lambda x: x[1])
    return sorted_records[:k]
```


The function min_k takes a list of tuples (records) and an integer k as input. It returns a list of tuples representing the k records with the smallest values in the second element of the tuple.

The function uses the built-in sorted function to sort the records based on the second element of the tuple. It then returns the first k elements of the sorted list, which are the k records with the smallest values.

This function assumes that the input list is not empty and that k is a positive integer less than or equal to the length of the input list. If k is greater than the length of the input list, the function will return the entire list. If k is zero, the function will return an empty list.

The unit test `assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]` ensures that the function returns the expected result for the given input. The test case checks that the function returns the two records with the smallest values in the second element of the tuple.