
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split(" ")
    primes = [i for i in range(2, len(sentence)+1) if is_prime(i)]
    result = []
    for word in words:
        if len(word) in primes:
            result.append(word)
    return " ".join(result)

print(words_in_sentence("This is a test"))
print(words_in_sentence("lets go for swimming"))




def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split(" ")
    primes = [i for i in range(2, len(sentence)+1) if is_prime(i)]
    result = []
    for word in words:
        if len(word) in primes:
            result.append(word)
    return " ".join(result)

print(words_in_sentence("This is a test"))
print(words_in_sentence("lets go for swimming"))




# Time Complexity: O(nlog(logn))
# Space Complexity: O(1)

# This solution uses a pre-calculated list of prime numbers up to the length of the input sentence,
# and checks if the length of each word in the sentence is in the list of prime numbers.
# The time complexity of the solution is determined by the time complexity of the is_prime function,
# which is O(log(logn)) for small inputs and O(n) for large inputs.
# However, since the maximum length of a word in the sentence is 100, the time complexity of the solution is O(nlog(logn)),
# where n is the length of the sentence.
# The space complexity of