def words_in_sentence(sentence):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    result = ' '.join([word for word in words if is_prime(len(word))])
    return result

# Example 1
sentence1 = "This is a test"
print(words_in_sentence(sentence1))  # Output: "is"

# Example 2
sentence2 = "lets go for swimming"
print(words_in_sentence(sentence2))  # Output: "go for"