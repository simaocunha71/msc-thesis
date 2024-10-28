    import re

    count = 0
    index = 0
    while index < len(S):
        if S[index] == 'I':
            if index+1 < len(S) and (S[index+1] == '?' or S[index+1] == '.' or S[index+1] == '!'):
                count += 1
        index += 1
    return count



# Other solutions:
# def is_bored(S):
#     count = 0
#     for word in re.split(r'[.?!]', S):
#         if word.lower() == "i":
#             count += 1
#     return count

# Alternative:
# def is_bored(S):
#     """
#     You'll be given a string of words, and your task is to count the number
#     of boredoms. A boredom is a sentence that starts with the word "I".
#     Sentences are delimited by '.', '?', or '!'.
#     """
#     return len(re.findall('I\s*[.?!]', S))


# Alternative:
# def is_bored(S):
#     """
#     You'll be given a string of words, and your task is to count the number
#     of boredoms. A boredom is a sentence that starts with the word "I".
#     Sentences are delimited by '.', '?', or '!'.
#     """
#     return len(re.findall('(I\s*\.)|(I\s*\?)|(I\s*!)', S))






















































































































