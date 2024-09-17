```
def reverse_words(s):
    return ' '.join(s.split()[::-1])
```
The function `reverse_words` takes a string `s` as an argument. It splits the string into a list of words using the `split` method, which splits a string into a list where each word is a list item. The `[::-1]` is used to reverse the list. Then it joins the list of words back into a string with a space in between each word using the `join` method. The result is the input string with the words in reverse order. 

For example, if the input string is "python program", the function will return "program python".  The unit test `assert reverse_words("python program")==("program python")` ensures this function works correctly. 