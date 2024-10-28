
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split(" ")
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result.strip()

# Test
print(words_in_sentence("This is a test"))  # "is"
print(words_in_sentence("lets go for swimming"))  # "go for"

# Time Complexity: O(n*log(logn))
# Space Complexity: O(n)

# The time complexity is dominated by checking the primality of the number, which can be done in O(log(logn)) time.
# The space complexity is O(n) as we are storing all the words in the sentence.

# Here's a Python implementation of the Sieve of Eratosthenes algorithm to check primality in O(n*log(logn)) time.

```python
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split(" ")
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result.strip()
```

This implementation uses the Sieve of Eratosthenes algorithm to check the primality of a number in O(n*log(logn)) time. It iterates through all the numbers up to the given number and marks the multiples of each number as composite. Finally, it checks if the given number is marked as composite. If not, then it is a prime number, and the function returns True.

The space complexity of this implementation is O(n) because it uses a boolean array of size n to mark the multiples of each number as composite.

The time complexity of