```python
def words_in_sentence(sentence):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    return ' '.join(word for word in words if is_prime(len(word)))
```

Explanation:
The function `words_in_sentence` takes a string `sentence` as input and splits it into a list of words using the `split` method. Then, it iterates over each word in the list and checks if the length of the word is a prime number using the `is_prime` helper function. If the length is a prime number, the word is added to a new list. Finally, the function joins the words in the new list into a string using the `join` method and returns the result.

The `is_prime` helper function checks if a number `n` is prime by iterating from 2 to the square root of `n` and checking if `n` is divisible by any number in that range. If `n` is divisible by any number, it is not prime and the function returns `False`. Otherwise, it returns `True`.

The time complexity of this solution is O(n * sqrt(m)), where n is the number of words in the sentence and m is the maximum length of a word. This is because the `is_prime` function has a time complexity of O(sqrt(m)) and it is called for each word in the sentence. The space complexity is O(n) because the solution uses a list to store the words.