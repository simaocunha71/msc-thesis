
def is_prime(n):
    # Check if a number is prime
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Create an empty string to store the result
    result = ""
    # Iterate through the words
    for word in words:
        # Check if the length of the word is a prime number
        if is_prime(len(word)):
            # If it is a prime number, append the word to the result
            result += word + " "
    # Return the result
    return result.strip()

# Test the function
print(words_in_sentence("This is a test"))  # Output: "is"
print(words_in_sentence("lets go for swimming"))  # Output: "go for"





def is_prime(n):
    # Check if a number is prime
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Create an empty string to store the result
    result = ""
    # Iterate through the words
    for word in words:
        # Check if the length of the word is a prime number
        if is_prime(len(word)):
            # If it is a prime number, append the word to the result
            result += word + " "
    # Return the result
    return result.strip()

# Test the function
print(words_in_sentence("This is