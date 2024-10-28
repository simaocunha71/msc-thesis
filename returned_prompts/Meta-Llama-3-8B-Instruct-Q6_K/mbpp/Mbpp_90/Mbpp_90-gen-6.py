```
def len_log(word_list):
    return max(len(word) for word in word_list)
```
This function uses a generator expression to iterate over each word in the list, calculates the length of each word using the len() function, and then uses the built-in max() function to find the longest word. The length of the longest word is then returned.

The unit test `assert len_log(["python","PHP","bigdata"]) == 7` ensures that the function works correctly, as the longest word in the list is "bigdata" with a length of 7. 