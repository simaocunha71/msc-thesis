
def is_consonant(x):
    return not (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == ' ')

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        if len([x for x in word if is_consonant(x)]) == n:
            result.append(word)
    return result

# Alternative solution:
# def select_words(s, n):
#     words = s.split()
#     result = []
#     for word in words:
#         if len(set([x for x in word if is_consonant(x)])) == n:
#             result.append(word)
#     return result

# Alternative solution:
# def select_words(s, n):
#     words = s.split()
#     result = []
#     for word in words:
#         if len([x for x in word if is_consonant(x)]) == n:
#             result.append(word)
#     return result


def is_consonant(x):
    return not (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == ' ')

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        if len([x for x in word if is_consonant(x)]) == n:
            result.append(word)
    return result

# Alternative solution:
# def select_words(s, n):
#     words = s.split()
#     result = []
#     for word in words:
#         if len(set([x for x in word if is_consonant(x)])) == n:
#             result.append(word)
#     return result

# Alternative solution:
# def select_words(s, n):
#     words = s.split()
#     result = []
#     for word in