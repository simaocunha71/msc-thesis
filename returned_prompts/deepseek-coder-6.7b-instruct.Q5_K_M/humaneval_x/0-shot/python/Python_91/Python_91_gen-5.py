
    S = S.split('. ')
    count = 0
    for sentence in S:
        if sentence[0] == 'I':
            count += 1
    return count

print(is_bored("Hello world"))  # 0
print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # 1
print(is_bored("I am bored. I want to go home. What should I do?"))  # 2

"""
This program works by splitting the input string into a list of sentences.
Then it iterates through each sentence, checking if the first word is "I".
If it is, it increments the count. Finally, it returns the count.
"""