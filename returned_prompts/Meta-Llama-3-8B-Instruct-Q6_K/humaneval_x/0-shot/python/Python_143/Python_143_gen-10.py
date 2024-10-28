
The task is to create a function that takes a sentence as input and returns a new sentence containing only the words from the original sentence whose lengths are prime numbers. The order of the words in the new sentence should be the same as the original one.

Here's the Python code that accomplishes this:

```
def words_in_sentence(sentence):
    words = sentence.split()
    prime_words = []
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)
    return ' '.join(prime_words)


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

In this code, the `words_in_sentence` function splits the input sentence into individual words and checks each word's length to see if it's prime using the `is_prime` function. If the length is prime, the word is added to a list of prime words. Finally, the function joins the list of prime words into a single string and returns it.

The `is_prime` function checks if a given number is prime by iterating up to the square root of the number and checking if the number is divisible by any of the numbers in that range. If the number is divisible, it's not prime. If it's not divisible, it's prime.

You can test this code using the examples provided:

```
print(words_in_sentence("This is a test"))  # Output: "is"
print(words_in_sentence("lets go for swimming"))  # Output