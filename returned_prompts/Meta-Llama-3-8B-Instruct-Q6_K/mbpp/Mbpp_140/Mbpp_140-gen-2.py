```
def extract_singly(lst):
    flat_list = [item for sublist in lst for item in sublist]
    return set(flat_list)
```


The function `extract_singly` takes a list of lists as input and returns a set of unique numbers. It first flattens the list of lists into a single list using a list comprehension, and then converts this list into a set. The set data structure in Python is an unordered collection of unique elements. This is useful for removing duplicates and converting the list of lists into a single set of numbers. The unit test `assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])` ensures that the function works correctly by comparing the output with the expected output. 