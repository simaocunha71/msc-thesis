You can solve this problem by using a list comprehension to extract the rear element of each tuple. The rear element is the last element in each tuple, which you can access using the index -1.

Here's the solution:
```
def rear_extract(tuples_list):
    return [t[-1] for t in tuples_list]
```
This function takes a list of tuples as input, and for each tuple, it extracts the rear element (i.e., the last element) and adds it to the output list. The result is a list containing the rear element of each tuple.

The unit test `assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]` confirms that this function works correctly. It checks that the output of the function is `[21, 20, 19]` when the input is `[(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]`. Since the rear element of each tuple is the last element, the output is indeed correct.