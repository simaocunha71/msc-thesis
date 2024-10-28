```
def len_log(words):
    return max(len(word) for word in words)
```


The function len_log takes a list of words as input and returns the length of the longest word. The max function is used with a generator expression to find the maximum length of the words in the list. The len function is used to get the length of each word. The unit test `assert len_log(["python","PHP","bigdata"]) == 7` ensures that the function returns the correct result. 

For example, if the input list is ["python","PHP","bigdata"], the function will return 7, which is the length of the longest word "bigdata". 

This function works for lists of any length, not just for the specific list used in the unit test. It will find the longest word in the list regardless of the number of words in the list. 

The time complexity of this function is O(n), where n is the number of words in the list, because it needs to iterate over each word in the list to find the longest one. The space complexity is O(1), because it only uses a constant amount of space to store the maximum length, regardless of the size of the input list. 