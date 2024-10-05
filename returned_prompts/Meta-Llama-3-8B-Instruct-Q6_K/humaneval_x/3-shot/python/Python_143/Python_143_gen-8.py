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
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True
# test
print(words_in_sentence("This is a test"))  # "is"
print(words_in_sentence("lets go for swimming"))  # "go for"  # test
print(words_in_sentence("This is a  test"))  # ""  # test
print(words_in_sentence("prime  test"))  # "prime test"
print(words_in_sentence("abc"))  # "abc"
print(words_in_sentence("a"))  # "a"
print(words_in_sentence(""))  # ""  # test
print(words_in_sentence("prime"))  # "prime"
print(words_in_sentence("is"))  # "is"  # test
print(words_in_sentence("a b"))  # "a b"  # test
print(words_in_sentence("a b c"))  # "a b c"  # test
print(words_in_sentence("a b c d"))  # "a b c d"  # test
print(words_in_sentence("a b c d e"))  # "a b c d e"  # test
print(words_in_sentence("a b c d e f"))  # "a b c d e f"  # test
print(words_in_sentence("a b c d e f g"))  # "a b c d e f g"  # test
print(words_in_sentence("a b c d e f g h"))  # "a b c d e f g h"  # test
print(words_in_sentence("a b c d e f g h i"))  # "a b c d e f g h i"  # test
print(words_in_sentence("a b c d e f g h i j"))  # "a b c d e f g h i j"  # test
print(words_in_sentence("a b c d e f g h i j k"))  #