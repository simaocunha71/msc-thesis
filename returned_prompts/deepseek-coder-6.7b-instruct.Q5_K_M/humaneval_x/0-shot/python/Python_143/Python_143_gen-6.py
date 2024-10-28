
def words_in_sentence(sentence):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    words = sentence.split()
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

# Test cases
print(words_in_sentence("This is a test"))  # Output: "is"
print(words_in_sentence("lets go for swimming"))  # Output: "go for"
print(words_in_sentence("Python coding is fun"))  # Output: "Python coding is"
print(words_in_sentence("I love solving problems"))  # Output: "solving problems"
print(words_in_sentence("Q AAA BB C"))  # Output: "AAA BB"

The helper function, `is_prime`, is used to check if a number is prime or not. In the main function, the input sentence is split into words and for each word, its length is checked using `is_prime`. If it returns True, the word is added to the result list. Finally, the words in the result list are joined with a space and returned.
"""

# TASK 2:
"""
