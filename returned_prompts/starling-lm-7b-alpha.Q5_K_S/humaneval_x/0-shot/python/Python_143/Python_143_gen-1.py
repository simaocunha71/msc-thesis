
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def words_in_sentence(sentence):
    words = sentence.split(" ")
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result.strip()



# Other solutions:
# def words_in_sentence(sentence):
#     return " ".join(word for word in sentence.split() if all(word[i] == word[0] for i in range(1, len(word))))

# def words_in_sentence(sentence):
#     return " ".join(word for word in sentence.split() if len(word) in {2, 3, 5})

# def words_in_sentence(sentence):
#     words = sentence.split()
#     return " ".join(word for word in words if len(word) in {2, 3, 5})

# def words_in_sentence(sentence):
#     return " ".join(word for word in sentence.split() if all(word[i] == word[0] for i in range(1, len(word))))

# def words_in_sentence(sentence):
#     words = sentence.split(" ")
#     return " ".join(word for word in words if len(word) in {2, 3, 5})

# def words_in_sentence(sentence):
#     return " ".join(word for word in sentence.split() if any(char == word[0] for char in word))

# def words_in_sentence(sentence):
#     words = sentence.split(" ")
#     return " ".join(word for word in words if len(set(word)) == 1)

# def words_in_sentence(sentence):
#     return " ".join(word for word in sentence.split() if len(set(word)) == 