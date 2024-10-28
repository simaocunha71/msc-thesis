```
def words_in_sentence(sentence):
    prime_words = []
    sentence = sentence.split()
    for word in sentence:
        if is_prime(len(word)):
            prime_words.append(word)
    return ' '.join(prime_words)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```


The function `words_in_sentence` takes a sentence as input and returns a new string containing only the words from the original sentence whose lengths are prime numbers. The order of the words in the new string is the same as the original one.

The function `is_prime` checks whether a given number is prime or not. It returns `True` if the number is prime and `False` otherwise.

The `words_in_sentence` function splits the input sentence into words, checks the length of each word to see if it's prime, and if it is, adds it to the `prime_words` list. Finally, it joins the `prime_words` list into a string with spaces in between and returns the result.

Example:
```
print(words_in_sentence("This is a test"))  # Output: "is"
print(words_in_sentence("lets go for swimming"))  # Output: "go for"
```


Note: This solution assumes that the input sentence contains only letters. If the sentence can contain other characters, additional processing may be needed to handle them correctly.