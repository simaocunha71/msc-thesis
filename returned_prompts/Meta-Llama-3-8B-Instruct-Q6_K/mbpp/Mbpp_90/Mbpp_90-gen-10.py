```
def len_log(lst):
    return max(len(word) for word in lst)
```
The function takes a list of words as input and returns the length of the longest word. It uses a generator expression to iterate over the words in the list, calculate the length of each word, and then returns the maximum length. 

The unit test `assert len_log(["python","PHP","bigdata"]) == 7` ensures that the function works correctly by comparing the length of the longest word in the input list with the expected length. 

This function assumes that the input list is not empty. If the input list could be empty, it's a good idea to add a check for that case and return a suitable value (e.g., 0) if the list is empty. 

Here is the updated function:
```
def len_log(lst):
    if not lst:
        return 0
    return max(len(word) for word in lst)
```  # Python 3.9 and later
```
def len_log(lst):
    if not lst:
        return 0
    return max((len(word) for word in lst), default=0)  # Python 3.8 and earlier
```  # Python 3.8 and earlier
In the above code, `default=0` is used to return 0 in case the input list is empty. This is a feature of the `max` function in Python 3.8 and later. In earlier versions of Python, you can use the `if not lst` check to return 0 if the list is empty.  # Python 3.8 and earlier
```
def len_log(lst):
    if not lst:
        return 0
    return max((len(word) for word in lst), default=0)  # Python 3.8 and earlier
```  # Python 3.8 and earlier
In the above code, `default=0` is used to return 0 in case the input list is empty. This is a feature of the `max` function in Python 3.8 and later. In earlier versions of Python, you can use the `if not lst` check to return 0 if the list is empty.  # Python 3.8 and earlier
```
def len_log(lst):
    if not lst:
        return 0
    return max(len(word) for word in lst)
```  # Python 3.9 and later
```
