Here is a Python solution that uses list comprehension and the `isprime` function to filter out the words with prime length and join the remaining words into a string:

```python
def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def WordsInSentence(sentence):
    words = sentence.split()
    result = [word for word in words if isprime(len(word))]
    return ' '.join(result)

print(WordsInSentence("This is a test"))  # Output: "is"
print(WordsInSentence("lets go for swimming"))  # Output: "go for"
```

In this solution, we first split the sentence into words using the `split` function. Then, we use a list comprehension to filter out the words whose lengths are not prime numbers. The `isprime` function checks if a number is prime. Finally, we join the remaining words into a string using the `join` function. The `result` variable will contain the words whose lengths are prime numbers. We can then return this string.

This solution has a time complexity of O(n*m), where n is the number of words in the sentence and m is the maximum length of a word. This is because we are iterating over each word and checking its length to see if it is prime. The space complexity is O(n), as we are storing the filtered words in the `result` list.