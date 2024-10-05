```
def sorted_list_sum(lst):
    # filter out the strings with odd lengths
    lst = [s for s in lst if len(s) % 2 == 0]
    
    # sort the list by length of each word and then alphabetically
    lst.sort(key=lambda x: (len(x), x))
    
    return lst
```



The function sorted_list_sum() takes a list of strings as input, filters out the strings with odd lengths, and returns the resulted list in sorted order. The list is sorted by the length of each word in ascending order, and if two words have the same length, they are sorted alphabetically.

The unit tests provided ensure that the function works correctly. For example, the test case assert list_sort(["aa", "a", "aaa"]) => ["aa"] checks that the function filters out the strings with odd lengths and returns the resulted list in sorted order. Similarly, the test case assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"] checks that the function sorts the list by length of each word and then alphabetically.

The function uses a list comprehension to filter out the strings with odd lengths. It then uses the sort() method with a lambda function as the key to sort the list. The lambda function returns a tuple for each string, where the first element is the length of the string and the second element is the string itself. This allows the list to be sorted by length first, and then alphabetically. Finally, the function returns the sorted list.