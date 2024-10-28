    prime_words = ""

    for word in sentence.split(" "):
        if all(word[i] == 'a' for i in range(len(word))):
            continue
        if len(word) in primes:
            prime_words += word + " "

    return prime_words.strip()


def primes(n):
    """
    Returns an infinite generator yielding primes.
    >>> primes(10)
    <generator at ...>
    >>> primes_list = list(primes(10))
    >>> primes_list
    [2, 3, 5, 7]
    """
    if n < 2:
        return
    is_prime = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    for i in range(3, n, 2):
        if is_prime[i]:
            yield i




# def words_in_sentence(sentence):
#     """
#     You are given a string representing a sentence,
#     the sentence contains some words separated by a space,
#     and you have to return a string that contains the words from the original sentence,
#     whose lengths are prime numbers,
#     the order of the words in the new string should be the same as the original one.

#     Example 1:
#         Input: sentence = "This is a test"
#         Output: "is"

#     Example 2:
#         Input: sentence = "lets go for swimming"
#         Output: "go for"

#     Constraints:
#         * 1 <= len(sentence) <= 100
#         * sentence contains only letters
#     """

#     primes_words = ""

#     for word in sentence.split(" "):
#         if all(word[i] == 'a' for i in range(len(word))):
#             continue
#         if len(word)