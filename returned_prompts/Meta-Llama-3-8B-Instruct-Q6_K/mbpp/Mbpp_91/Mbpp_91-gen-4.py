```
def find_substring(lst, substring):
    return any(substring in s for s in lst)
```
This function uses the built-in any() function and a generator expression to check if the substring is present in any of the strings in the list. The any() function returns True if at least one element of the iterable is true. If not found, it returns False. 

For example, if the list is ["red", "black", "white", "green", "orange"] and the substring is "ack", the function will return True because "ack" is present in "black". If the substring is "xyz" and the list is the same, the function will return False because "xyz" is not present in any of the strings in the list. 