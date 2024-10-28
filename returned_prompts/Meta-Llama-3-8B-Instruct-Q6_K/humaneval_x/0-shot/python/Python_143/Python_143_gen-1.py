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
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
```
Explanation:
The function `words_in_sentence` takes a sentence as input and returns a string containing the words whose lengths are prime numbers. It first splits the sentence into words, then iterates over each word. For each word, it checks if the length of the word is prime using the `is_prime` function. If the length is prime, it adds the word to the result list. Finally, it joins the result list into a string with spaces and returns it.

The `is_prime` function checks if a given number is prime. It returns `True` if the number is prime, and `False` otherwise. It uses a simple algorithm to check for primality: it checks if the number is less than or equal to 1 (in which case it's not prime), if it's 2 (in which case it's prime), or if it's divisible by any odd number up to its square root (in which case it's not prime). If none of these conditions are met, it returns `True`, indicating that the number is prime.