```
def sorted_list_sum(lst):
    lst = [s for s in lst if len(s) % 2 == 0]
    return sorted(lst, key=lambda x: (len(x), x))
```


The unit tests provided help to clarify the problem. For example, the test `assert list_sort(["aa", "a", "aaa"]) => ["aa"]` shows that the function should return a list of strings in sorted order, and the test `assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]` shows that the function should return a list of strings in sorted order, even if it has duplicates.

The function `sorted_list_sum` takes a list of strings as input, removes the strings that have odd lengths from the list, and returns the resulted list in sorted order. The sorting is done based on two criteria: the length of the string, and the string itself. If two strings have the same length, they are sorted alphabetically.

Here is the Python code for the function:
```
def sorted_list_sum(lst):
    lst = [s for s in lst if len(s) % 2 == 0]
    return sorted(lst, key=lambda x: (len(x), x))
```
The function uses a list comprehension to remove the strings with odd lengths from the input list. Then it uses the built-in `sorted` function to sort the list based on the criteria specified above. The `key` argument of the `sorted` function is a lambda function that returns a tuple for each string in the list. The tuple contains the length of the string and the string itself. The `sorted` function uses this tuple to determine the order of the strings. If two strings have the same length, the `sorted` function uses the second element of the tuple (the string itself) to break the tie and sort the strings alphabetically.