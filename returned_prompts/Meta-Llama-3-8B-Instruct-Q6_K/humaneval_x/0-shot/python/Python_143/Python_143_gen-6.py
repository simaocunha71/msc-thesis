```
def words_in_sentence(sentence):
    result = ""
    words = sentence.split()
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result.strip()
```

Explanation:
The function `words_in_sentence` takes a sentence as input, splits it into words, and then checks each word's length to see if it's a prime number. If it is, the word is added to the result string. The result string is then returned, stripped of any trailing spaces.

The `is_prime` function is not provided in the problem statement, but it can be defined as follows:

```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, it's not prime, and the function returns `False`. Otherwise, it returns `True`. The reason we only need to check up to the square root of the number is that a larger factor of the number would be a multiple of a smaller factor that has already been checked. This makes the function more efficient.