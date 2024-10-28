
Here is the Python code to solve the problem:

```python
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
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(words_in_sentence("This is a test"))  # Output: "is"
print(words_in_sentence("lets go for swimming"))  # Output: "go for"
```

Explanation:

1. The `words_in_sentence` function takes a sentence as input, splits it into words, and then iterates over each word.
2. For each word, it checks if the length of the word is a prime number using the `is_prime` function.
3. If the length of the word is a prime number, the word is added to the `result` list.
4. Finally, the `result` list is joined into a string with spaces in between and returned as the output.

The `is