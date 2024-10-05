
from itertools import filterfalse, tee

def words_in_sentence(sentence):
    words = sentence.split()
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = filterfalse(lambda x: not is_prime(x), range(1, len(words) + 1))
    a, b = tee(primes)
    next(b, None)
    return ' '.join(words[i] for i in a) + ' ' + ' '.join(words[i] for i in b)

def words_in_sentence(sentence):
    words = sentence.split()
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for i, word in enumerate(words):
        if is_prime(i + 1):
            primes.append(word)

    return ' '.join(primes)

def words_in_sentence(sentence):
    words = sentence.split()
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = filterfalse(lambda x: not is_prime(x), range(1, len(words) + 1))
    a, b = tee(primes)
    next(b, None)
    return ' '.join(words[i] for i in a) + ' ' + ' '.join(words[i] for i in b)

def words_in_sentence(sentence):
    words = sentence.split()
    def is_prime(n):
        if n <= 1: