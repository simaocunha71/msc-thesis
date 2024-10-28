
    def words_in_sentence(sentence):
        def is_prime(n):
            if n == 1:
                return False
            for i in range(2, int(n ** 0.5) + 1):
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


In this solution, the function `is_prime(n)` checks if a number is a prime number or not. The main function `words_in_sentence(sentence)` splits the input sentence into words, checks each word's length and checks if it's a prime number, if it is, it appends it to the result list. Finally, it joins the result list into a string with a space in between the words and returns the result.
'''

def words_in_sentence(sentence):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
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

'''
