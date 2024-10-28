```
def len_log(words):
    return max(len(word) for word in words)
``` 
Explanation:
The function `len_log` takes a list of words as an argument. It uses a generator expression to iterate over each word in the list, calculates the length of each word using the `len` function, and then finds the maximum length using the `max` function. The result is returned as the length of the longest word. 

The unit test `assert len_log(["python","PHP","bigdata"]) == 7` checks that the function returns the correct result. In this case, the longest word is "bigdata" which has a length of 7. 

This function works with a list of words. If you want to find the length of the longest word in a string, you would need to split the string into a list of words first. For example: `max(len(word) for word in "python PHP bigdata".split())`.  However, based on the provided unit test, it seems that the function should work with a list of words.  Therefore, the function above should work as expected.  If the function is supposed to work with a string instead of a list of words, the function would need to be modified accordingly.  For example: `max(len(word) for word in input_string.split())`.  In this case, `input_string` would be the string that you want to find the longest word in.  The function would split the string into a list of words using the `split` method, then find the longest word using the same approach as before.  The result would be the length of the longest word in the string.  



Please note that this solution assumes that words are separated by spaces. If words can be separated by other characters (like commas, tabs, etc.), you would need to adjust the `split` method accordingly. For example, if words can be separated by commas, you would use `input_string.split(',')`. If words can be separated by tabs, you would use `input_string.split('\t')`. And so on.  



Also, this solution assumes that words are sequences of alphanumeric characters. If words can contain other characters (like punctuation, etc.), you might need to adjust the `max` function accordingly. For example, if you want to ignore punctuation, you could use a list comprehension to remove punctuation from each word before calculating its length. For example: `max(len(word.strip(string.punctuation)) for word in input