```
def all_Characters_Same(s):
    return len(set(s)) == 1
```
This function uses Python's built-in set data structure, which removes duplicates. If the length of the set is 1, it means all characters in the string are the same. Otherwise, it means there are different characters in the string. The unit test `assert all_Characters_Same("python") == False` ensures that the function returns False when all characters are not the same. 

Note: The function is case sensitive and considers spaces and punctuation as characters. If you want to ignore case, spaces, and punctuation, you can preprocess the string to remove or normalize these. For example, you can convert the string to lowercase and remove spaces and punctuation. Here's how you can do it:

```
def all_Characters_Same(s):
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    return len(set(s)) == 1
```  