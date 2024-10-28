
def words_in_sentence(sentence):
    sentence = sentence.split(' ')
    words = []
    for word in sentence:
        if is_prime(len(word)):
            words.append(word)
    return ' '.join(words)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# time complexity: O(n * sqrt(n))
# space complexity: O(1)

# Optimized Solution:

def words_in_sentence(sentence):
    sentence = sentence.split(' ')
    words = []
    for word in sentence:
        if is_prime(len(word)):
            words.append(word)
    return ' '.join(words)


def is_prime(n):
    if n < 2:
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

# time complexity: O(n * log(n))
# space complexity: O(1)

# Optimized Solution:

def words_in_sentence(sentence):
    sentence = sentence.split(' ')
    words = []
    for word in sentence:
        if is_prime(len(word)):
            words.append(word)
    return ' '.join(words)


def is_prime(n):
    if n < 2:
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

# time complexity: O(n * sqrt(n))
# space complexity: O(1)

# Optimized