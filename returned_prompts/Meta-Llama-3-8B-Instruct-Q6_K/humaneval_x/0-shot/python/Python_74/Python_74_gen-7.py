```
def total_match(lst1, lst2):
    total1 = sum(len(i) for i in lst1)
    total2 = sum(len(i) for i in lst2)
    
    if total1 < total2:
        return lst1
    elif total1 > total2:
        return lst2
    else:
        return lst1
```



The function total_match takes two lists of strings as input and returns the list with the total number of characters in its strings less than the other list. If the two lists have the same total number of characters, it returns the first list.

It calculates the total number of characters in each list by summing the lengths of all strings in the list.

Then it compares the totals. If the total of the first list is less than the total of the second list, it returns the first list. If the total of the first list is greater than the total of the second list, it returns the second list. If the totals are equal, it returns the first list.

This function works correctly for the given examples. For example, total_match(['hi', 'admin'], ['hI', 'Hi']) returns ['hI', 'Hi'] because 'hI' and 'Hi' have a total of 3 characters, which is less than the total of 9 characters in ['hi', 'admin']. Similarly, total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) returns ['hi', 'admin'] because 'hi', 'admin' have a total of 6 characters, which is less than the total of 14 characters in ['hi', 'hi', 'admin', 'project']. 

The function also works correctly for the edge case where one of the lists is empty, as in total_match([], []). In this case, the function returns an empty list because the total number of characters in an empty list is 0. 





The function total_match is written in a simple and efficient way, with a time complexity of O(n), where n is the total number of strings in the input lists. This is because it iterates over each string in the lists once to calculate the total number of characters. The space complexity is O(1), which means the function uses a constant amount of space, because it only uses a few variables to store the totals and the lists themselves. 