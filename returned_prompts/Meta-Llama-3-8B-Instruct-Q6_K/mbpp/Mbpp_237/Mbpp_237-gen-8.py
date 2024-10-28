```
def check_occurences(tuples_list):
    from collections import Counter
    counter = Counter(tuples_list)
    result = {}
    for key, value in counter.items():
        result[key] = value
    return result
```


Explanation:
The problem requires a function that takes a list of tuples as input and returns a dictionary where each unique tuple is mapped to its frequency in the list. 

To solve this, we can use the Counter class from the collections module in Python, which is a dictionary subclass for counting hashable objects. 

Here's the solution:
1. Import the Counter class from the collections module.
2. Create an instance of Counter and pass the list of tuples to it.
3. Convert the Counter object to a dictionary.
4. Return the dictionary.

The unit test `assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}` ensures that the function works correctly. It checks if the output of the function for the given input is as expected. If the output matches the expected result, the test passes; otherwise, it fails. 