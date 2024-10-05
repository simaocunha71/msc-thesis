
def words_in_sentence(sentence):
    words = sentence.split()
    return ' '.join(word for word in words if is_prime(len(word)))

def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))
