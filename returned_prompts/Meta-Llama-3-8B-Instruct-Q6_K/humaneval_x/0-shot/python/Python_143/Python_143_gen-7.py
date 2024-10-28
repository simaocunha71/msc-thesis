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

*   The function `words_in_sentence` takes a sentence as input, splits it into words, and then checks each word's length to see if it's a prime number. If it is, the word is added to the `result` list.
*   The function `is_prime` is a helper function that checks if a given number is prime. It does this by checking divisibility up to the square root of the number.
*   Finally, the function `words_in_sentence` joins the `result` list into a string, separated by spaces, and returns the result.

This solution has a time complexity of O(n), where n is the number of words in the sentence, because it iterates over each word once. The space complexity is also O(n), because it stores the result in a list. The `is_prime` function has a time complexity of O(sqrt(n)), but this is dominated by the overall time complexity of the `words_in_sentence` function.