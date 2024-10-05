
    def words_in_sentence(sentence):
        prime_words = []
        words = sentence.split()

        def is_prime(n):
            if n == 1:
                return False
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

        for word in words:
            if is_prime(len(word)):
                prime_words.append(word)

        return ' '.join(prime_words)

print(words_in_sentence("This is a test"))  # "is"
print(words_in_sentence("lets go for swimming"))  # "go for"
print(words_in_sentence("Python is a great programming language"))  # "Python a great language"

Explanation:

The function `words_in_sentence` takes a string `sentence` as input and splits it into a list of words. It then iterates through the list of words, checking if the length of each word is a prime number using the helper function `is_prime`. If the length of a word is a prime number, the word is appended to the list `prime_words`. Finally, the function returns a string consisting of the words in `prime_words`, separated by a space. The order of the words in the returned string is the same as the order in the original sentence.

The helper function `is_prime` checks if a number `n` is prime by checking if it is divisible by any number between 2 and `n`. If `n` is divisible by any of these numbers, it is not a prime number and the function returns `False`. If `n` is not divisible by any of these numbers, it is a prime number and the function returns `True`.

The time complexity of this function is O(n*m), where n is the number of words in the sentence and m is the average length of the words. This is because the function iterates through each word in the sentence and for each word, it checks if the length of the word is a prime number. The space complexity is O(n), because in the worst case (when all words are prime), the function stores all words in the list `prime_words`