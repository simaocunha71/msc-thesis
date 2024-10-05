Here is a Python solution using list comprehension and the built-in sorted function to sort the list:

```Python
def list_sort(lst):
    return sorted([word for word in lst if len(word) % 2 == 0], key=lambda x: (len(x), x))
```

This function uses a list comprehension to create a new list that only includes the strings with even lengths. The sorted function is then used to sort this list, first by the length of each word, and then alphabetically. The key argument to the sorted function is a lambda function that returns a tuple for each word, with the length as the first element and the word itself as the second. This allows the sorted function to first sort by length, and then by word. 

For example, if you call `list_sort(["aa", "a", "aaa"])`, it will return `["aa"]`, and if you call `list_sort(["ab", "a", "aaa", "cd"])`, it will return `["ab", "cd"]`. 

The unit tests you provided, `assert list_sort(["aa", "a", "aaa"]) => ["aa"]` and `assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]`, will pass with this function. 

The time complexity of this function is O(n log n) due to the sorting operation, where n is the number of words in the list. The space complexity is O(n) because we are creating a new list to store the filtered and sorted words. 