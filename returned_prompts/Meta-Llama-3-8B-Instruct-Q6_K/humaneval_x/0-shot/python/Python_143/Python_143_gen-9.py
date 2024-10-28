
The problem is asking to write a function that takes a sentence as input and returns a new sentence that contains only the words from the original sentence whose lengths are prime numbers. The order of the words in the new sentence should be the same as the original one.

Here is the Python solution for this problem:

```
def words_in_sentence(sentence):
    words = sentence.split()
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)


def is_prime(n):
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

In this solution, we first split the input sentence into words. Then we iterate over each word and check if its length is prime using the `is_prime` function. If the length is prime, we add the word to the result list. Finally, we join the words in the result list with a space and return the resulting sentence.

The `is_prime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, then the number is not prime. If it is not divisible by any of these values, then the number is prime. This function is used to filter out the words with non-prime lengths. A word's length is considered prime if the `is_prime` function returns `True` for that length.