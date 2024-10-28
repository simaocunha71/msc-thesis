
    def words_in_sentence(sentence):
        # function to check if a number is prime
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        words = sentence.split()
        result = []
        for word in words:
            if is_prime(len(word)):
                result.append(word)
        return " ".join(result)

    print(words_in_sentence("This is a test"))  # Output: "is"
    print(words_in_sentence("lets go for swimming"))  # Output: "go for"


Explanation:

In the problem, we have to return a string of words from the given sentence whose lengths are prime numbers. We first split the sentence into words and for each word, we check if its length is a prime number by using the helper function `is_prime`. If it is, we add it to the result list. Finally, we join the words in the result list with spaces and return the result.

The helper function `is_prime` checks if a given number is prime by iterating from 2 to the square root of the number (inclusive) and checking if the number is divisible by any of these values. If it is divisible, it returns False, otherwise True, which indicates that the number is prime.

This solution has a time complexity of O(n*m) where n is the number of words in the sentence and m is the square root of the length of the longest word. This is because for each word, we are potentially iterating over up to its square root.

The space complexity is O(n) where n is the number of words in the sentence. This is because we are storing the words in a list.

This solution meets the problem's constraints.
"""

# 