```
def reverse_words(s):
    return ' '.join(s.split()[::-1])
```
This function works by first splitting the input string into a list of words using the `split` method. It then reverses the list of words using slicing (`[::-1]`) and finally joins the reversed list of words back into a string using the `join` method. The `' '` argument to the `join` method specifies that the words should be separated by a space. 

For example, if you call `reverse_words("python program")`, it will return `"program python"`. 

The unit test `assert reverse_words("python program")==("program python")` ensures that the function works correctly. 

This function assumes that the input string only contains spaces as separators. If the input string can contain other types of separators (e.g., commas, tabs, etc.), you would need to modify the function accordingly. 

Also, this function is case-sensitive, so it will preserve the original case of the words in the input string. If you want to reverse the case of the words as well, you can modify the function to use the `swapcase` method or the `upper` and `lower` methods.  For example, you could use `word.swapcase()` to reverse the case of each word.  However, this would depend on your specific requirements.  If you want to preserve the original case of the words, you can simply omit the case-reversing code.  



Here's how you could modify the function to reverse the case of the words as well:

```
def reverse_words(s):
    return ' '.join(word.swapcase() for word in s.split()[::-1])
```

This version of the function uses a generator expression to swap the case of each word before joining them back together. The `swapcase` method swaps the case of a string, so it converts uppercase letters to lowercase and vice versa. This ensures that the function not only reverses the order of the words, but also reverses their case.  



Here's how you could modify the function to reverse the case of the words as well, but only if the original case was uppercase:

```
def reverse_words(s):
    return ' '.join(word.upper() if word.isupper() else word.lower() for word in s.split()[::-1])
```

This version of the function uses a conditional expression to check whether each word is uppercase or lowercase. If the word is uppercase, it converts it to lowercase;