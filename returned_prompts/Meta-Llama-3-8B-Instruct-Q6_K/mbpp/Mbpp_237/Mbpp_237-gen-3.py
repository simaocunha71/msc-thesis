```
def check_occurences(lst):
    from collections import defaultdict
    d = defaultdict(int)
    for item in lst:
        d[tuple(sorted(item))] += 1
    return dict(d)
```



This function uses a defaultdict from the collections module to create a dictionary where the default value for each key is 0. It then iterates over the list of tuples, sorts each tuple (to ensure that tuples that are the same but in a different order are treated as the same), and increments the count for each tuple in the dictionary. Finally, it converts the defaultdict back to a regular dictionary and returns it.

The unit test provided ensures that the function works correctly. The expected output is a dictionary where each key is a unique tuple and the value is the number of times that tuple occurs in the list. The tuples are sorted before being used as keys in the dictionary, so that tuples that are the same but in a different order are treated as the same. For example, the tuples (3, 1) and (1, 3) are treated as the same because they are sorted to (1, 3) before being used as a key in the dictionary. 





Python code to solve the problem:

```
from collections import defaultdict

def check_occurences(lst):
    d = defaultdict(int)
    for item in lst:
        d[tuple(sorted(item))] += 1
    return dict(d)

assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
```





This code defines a function called `check_occurences` that takes a list of tuples as input and returns a dictionary where each key is a unique tuple and the value is the number of times that tuple occurs in the list. The function uses a defaultdict to create a dictionary where the default value for each key is 0, and then iterates over the list of tuples, sorting each tuple and incrementing the count for each tuple in the dictionary. Finally, it converts the defaultdict back to a regular dictionary and returns it.

The unit test provided ensures that the function works correctly. The expected output is a dictionary where each key is a unique tuple and the value is the number of times that tuple occurs in the list. The tuples are sorted before being used as keys