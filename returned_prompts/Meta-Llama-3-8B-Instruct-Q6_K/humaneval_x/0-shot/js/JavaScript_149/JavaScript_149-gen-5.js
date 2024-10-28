Here is a Python function that fulfills the requirements:

```Python
def list_sort(lst):
    return sorted([word for word in lst if len(word) % 2 == 0], key=lambda x: (len(x), x))
```

Explanation:
This function uses a list comprehension to filter out the words with odd lengths. It then uses the built-in sorted function to sort the list. The key argument of the sorted function is a lambda function that returns a tuple for each word. The first element of the tuple is the length of the word, and the second element is the word itself. This means that the list will be sorted first by the length of the words, and then by the words themselves. Since Python's sort is stable, this means that words with the same length will be sorted alphabetically. 

The unit test `assert list_sort(["aa", "a", "aaa"]) == ["aa"]` indicates that the function should return the list of strings in sorted order, and the test `assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]` indicates that the function should also sort the list alphabetically when two words have the same length. 

This function assumes that all words will have the same length, as stated in the problem. If the length of words can vary, this function will still work correctly. 

The time complexity of this function is O(n log n) due to the sorting operation, where n is the number of words in the input list. The space complexity is O(n) due to the creation of the new list. 