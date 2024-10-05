
Here is a Python solution that fulfills your requirements:
```
def select_words(s, n):
    s = s.split()  # split the string into a list of words
    result = []
    for word in s:
        consonants = 0
        for char in word:
            if char.lower() not in 'aeiou':  # check if the character is a consonant
                consonants += 1
        if consonants == n:  # if the word has exactly n consonants
            result.append(word)
    return result
```
This function works by iterating over each word in the input string, and then iterating over each character in the word. It checks if the character is a consonant by checking if it is not in the string 'aeiou' (which contains all the vowels). If the character is a consonant, it increments the `consonants` counter. After checking all characters in the word, it checks if the `consonants` counter is equal to the input `n`. If it is, it adds the word to the `result` list. Finally, it returns the `result` list, which contains all the words that have exactly `n` consonants.

Here is how you can test this function with the given examples:
```
print(select_words("Mary had a little lamb", 4))  # Output: ["little"]
print(select_words("Mary had a little lamb", 3))  # Output: ["Mary", "lamb"]
print(select_words("simple white space", 2))  # Output: []
print(select_words("Hello world", 4))  # Output: ["world"]
print(select_words("Uncle sam", 3))  # Output: ["Uncle"]
```
Note: This solution assumes that the input string contains only letters and spaces, as mentioned in the problem statement. If the input string can contain other characters, you may need to modify the solution