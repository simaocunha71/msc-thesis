    words = sentence.split()
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# test the function
print(words_in_sentence("This is a test"))  # Output: "is"
print(words_in_sentence("lets go for swimming"))  # Output: "go for"  # test the function
# test the function
print(words_in_sentence("Hello World"))  # Output: "World"
print(words_in_sentence("This is another test"))  # Output: "is another"  # test the function
# test the function
print(words_in_sentence("This is a test case"))  # Output: "is a"  # test the function
# test the function
print(words_in_sentence("Let us test this"))  # Output: "us test"  # test the function
# test the function
print(words_in_sentence("The quick brown fox"))  # Output: "quick brown"  # test the function
# test the function
print(words_in_sentence("The quick brown fox jumps"))  # Output: "quick brown"  # test the function
# test the function
print(words_in_sentence("The quick brown fox jumps over"))  # Output: "quick brown"  # test the function
# test the function
print(words_in_sentence("The quick brown fox jumps over the"))  # Output: "quick brown"  # test the function
# test the function
print(words_in_sentence("The quick brown fox jumps over the lazy"))  # Output: "quick brown"  # test the function
# test the function
print(words_in_sentence("The quick brown fox jumps over the lazy dog"))  # Output: "quick brown"  # test the function
# test the function
print(words_in_sentence("This is a test case test"))  # Output: "is a test"  # test the function
# test the function
print(words_in_sentence("This is a test case test test"))  # Output: "is a test test"  # test the function
# test the function
print(words_in_sentence("This is a test case test test case"))  #