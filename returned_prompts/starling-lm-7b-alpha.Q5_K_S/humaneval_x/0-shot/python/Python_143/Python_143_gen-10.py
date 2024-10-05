
def words_in_sentence(sentence):
    arr = sentence.split(' ')
    result = ''
    for word in arr:
        if is_prime(len(word)):
            result += word + ' '
    return result.strip()

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Alternative solution
def words_in_sentence(sentence):
    words = sentence.split()
    return " ".join(word for word in words if all(word[i] != ' ' for i in range(word.__len__() - 1)))

# Another alternative solution
def words_in_sentence(sentence):
    return " ".join(word for word in sentence.split(' ') if len(word) in (2, 3, 5))

# Another alternative solution
def words_in_sentence(sentence):
    return " ".join(word for word in sentence.split(' ') if any(x == 1 for x in prime_factors(len(word))))

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Another alternative solution
def words_in_sentence(sentence):
    return " ".join(word for word in sentence.split(' ') if any(x == 2 or x == 3 or x == 5 for x in prime_factors(len(word))))

# Another alternative solution
def words_in_sentence(sentence):
    primes_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47