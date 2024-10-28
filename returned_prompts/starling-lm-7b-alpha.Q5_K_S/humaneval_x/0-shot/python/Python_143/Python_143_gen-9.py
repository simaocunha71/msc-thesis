
def words_in_sentence(sentence):
    sentence = sentence.split(" ")
    res = ""
    for word in sentence:
        if len(word) in (2, 3, 5):
            res += word + " "
    return res.strip()

# Time: O(n)
# Space: O(1)


# Correct Solution:
def words_in_sentence(sentence):
    sentence = sentence.split(" ")
    res = ""
    for word in sentence:
        if all(word[i] != "3" for i in range(len(word)) if len(word) % (i + 1) == 0):
            res += word + " "
    return res.strip()

# Time: O(n)
# Space: O(1)


```


```
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    sentence = sentence.split(" ")
    res = ""
    for word in sentence:
        if is_prime(len(word)):
            res += word + " "
    return res.strip()

# Time: O(n * sqrt(n))
# Space: O(1)
```


```
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    sentence = sentence.split(" ")
    res = ""
    for word in sentence:
        if all(word[i] != "3" for i in range(len(word)) if len(word) % (i + 1) == 0):
            res += word + " "
    return res.strip()

# Time: O(n * sqrt(