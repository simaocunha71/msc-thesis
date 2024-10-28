```
def words_in_sentence(sentence):
    words = sentence.split()
    result = ''
    for word in words:
        if is_prime(len(word)):
            result += word + ' '
    return result.strip()

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
```
This code defines a function `words_in_sentence` that takes a sentence as input, splits it into words, and returns a string containing only the words whose lengths are prime numbers, in the same order as the original sentence.

The `is_prime` function is used to check if a number is prime. It returns `True` if the number is prime, and `False` otherwise.

In the `words_in_sentence` function, we iterate over each word in the sentence, check if its length is prime using the `is_prime` function, and if it is, we add the word to the result string.

Finally, we return the result string, stripping any trailing spaces using the `strip` method.