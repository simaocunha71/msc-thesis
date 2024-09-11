def replace_words(sentence, dictionary):
    words = sentence.split(' ')
    result = []
    for word in words:
        if word in dictionary:
            result.append(dictionary[word])
        else:
            result.append(word)
    return ' '.join(result)

# Testing
print(replace_words('The quick brown fox', {'The': 'It is', 'quick': 'slow'}))  # 'It is slow brown fox'

# Time Complexity: O(n)
# Space Complexity: O(n)


# Optimized Solution
def replace_words(sentence, dictionary):
    words = sentence.split(' ')
    result = [dictionary[word] if word in dictionary else word for word in words]
    return ' '.join(result