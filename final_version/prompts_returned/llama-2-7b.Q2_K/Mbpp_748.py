"""
Write a function to put spaces between words starting with capital letters in a given string.
assert capital_words_spaces("Python") == 'Python'
"""
def capital_words_spaces(string):
    """
    :param str string: An input string containing words separated by spaces. Words are defined as any contiguous sequence of alphabetic characters enclosed in double quotes.
    :return str: A space-separated version of the original string. Spaces are only added between lower case and upper case words.
    """
    if not isinstance(string, str): raise TypeError('Type Error: string must be a string type')
    
    def count_uppercase(s):
        return s.count("'") - (len(s) + len(s[::-1]))
    
    def check_lowercase(s):
        return s.count('"') == 0
        
    if sum(count_uppercase(string)) != len(string): raise ValueError('Value Error: length of string minus number of words is not equal to the number of upper case letters found in string.')
    
    def split_words():
        return wordwrap(s, width=32)  # break line into 30 chars or less per line on average
        
    if sum(check_lowercase(split_words())) != len(split_words()): raise ValueError('Value Error: number of words minus length of words is not equal to the number of upper case letters found in split words.')
    
    return ' '.join([word for word, position in string.split(" ") if count_uppercase(word) > 0 and check_lowercase(position + word) < len(string)])
```

### Output:
![](screenshot2.png)
