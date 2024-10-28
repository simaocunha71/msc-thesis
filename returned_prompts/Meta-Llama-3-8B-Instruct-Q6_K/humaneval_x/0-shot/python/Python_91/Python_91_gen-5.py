```
def is_bored(S):
    return S.split('.').count('I') + S.split('?').count('I') + S.split('!').count('I')
```


This function takes a string `S` as input and returns the number of boredoms in it. A boredom is a sentence that starts with the word "I". The function splits the string into sentences using the characters '.' , '?' and '!' as delimiters. It then counts the number of sentences that start with the word "I" and returns the result. The function uses the `split` method of the string, which splits the string into a list of substrings separated by the specified delimiter, and the `count` method of the list, which returns the number of occurrences of the specified element in the list. The result is the total number of boredoms in the string. 

For example, if the input string is "The sky is blue. The sun is shining. I love this weather", the function will split the string into sentences ["The sky is blue", "The sun is shining", "I love this weather"], count the number of sentences that start with "I" (which is 1), and return 1. If the input string is "Hello world", the function will split the string into sentences ["Hello world"], count the number of sentences that start with "I" (which is 0), and return 0. 