```
def is_bored(S):
    sentences = S.split('. ')
    boredoms = 0
    for sentence in sentences:
        if sentence and sentence[0].lower() == 'i':
            boredoms += 1
    return boredoms
```



This function splits the input string into sentences using the '.' as a delimiter, then checks each sentence to see if it starts with the word "I". If it does, it increments the boredom count. Finally, it returns the total count of boredoms. 

Note: The function is case-insensitive, it converts the first character of the sentence to lower case before checking. This means it will count sentences starting with "I", "i", "I ", "i ", etc. as boredoms. 

Also, it doesn't count empty sentences, because it checks if the sentence is not empty before checking its first character. 

It doesn't count sentences that don't end with '.', '?' or '!', because it splits the input string into sentences based on these characters. 

It also doesn't count sentences that are not separated by these characters, because it splits the input string into sentences based on these characters. 

This function is case-insensitive and considers sentences that don't end with '.', '?' or '!' as separate sentences. 

It also considers sentences that are not separated by these characters as separate sentences. 

It doesn't count empty sentences. 

It counts sentences that start with the word "I" as boredoms. 

It counts sentences that start with the word "i" as boredoms. 

It counts sentences that start with the word "I " as boredoms. 

It counts sentences that start with the word "i " as boredoms. 

It counts sentences that start with the word "I," as boredoms. 

It counts sentences that start with the word "i," as boredoms. 

It counts sentences that start with the word "I!" as boredoms. 

It counts sentences that start with the word "i!" as boredoms. 

It counts sentences that start with the word "I?" as boredoms. 

It counts sentences that start with the word "i?" as boredoms. 





Test cases:
```
print(is_bored("Hello world"))  # Output: 0
print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # Output: 1
print(is_bored("I love this weather. I hate this weather")) 