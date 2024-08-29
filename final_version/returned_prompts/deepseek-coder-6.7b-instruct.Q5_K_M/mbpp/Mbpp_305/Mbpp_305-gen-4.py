def start_withp(words_list):
    result = []
    for words in words_list:
        for word in words.split():
            if word[0].lower() == 'p':
                result.append(word)
    return tuple(result[:2])

print(start_withp(["Python PHP", "Java JavaScript", "c c++"]))

# Expected output:
# ('Python', 'PHP')

"""
The function `start_withp` goes through each string in the input list `words_list`, splits each string into words, and checks if each word starts with the letter 'p'. If it does, the word is added to the list `result`. The function returns the first two words in `result` as a tuple.
"""

"""
The function `start_withp` goes through each string in the input list `words_list`, splits each string into words, and checks if each word starts with the letter 'p'. If it does, the word is added to the list `result`. The function returns the first two words in `result` as a tuple.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
