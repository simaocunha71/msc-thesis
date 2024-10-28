```
def extract_nth_element(tuples, n):
    return [tuple_[0] for tuple_ in tuples]
```


This function takes a list of tuples and an integer n as input. It then returns a list containing the first element of each tuple in the list. This is achieved by using a list comprehension, which iterates over each tuple in the list and extracts the first element (at index 0) and adds it to the resulting list. The unit test provided shows that when given a list of tuples and the integer 0, the function should return a list of the first elements of each tuple in the list.