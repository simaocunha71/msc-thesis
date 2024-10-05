
from math import sqrt

def words_in_sentence(sentence):
    words = sentence.split()
    primes = [word for word in words if is_prime(word)]
    return ' '.join(primes)

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
