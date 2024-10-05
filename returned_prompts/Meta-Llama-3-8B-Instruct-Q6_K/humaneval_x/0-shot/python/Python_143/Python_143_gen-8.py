
Here is the Python solution for the problem. The `words_in_sentence` function splits the sentence into words and filters the words whose lengths are prime numbers. The `is_prime` function checks whether a number is prime or not.

```
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """

    prime_words = []
    words = sentence.split()
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)
    return ' '.join(prime_words)


def is_prime(n):
    """
    This function checks whether a number is prime or not.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True
```
In the `words_in_sentence` function, we first split the