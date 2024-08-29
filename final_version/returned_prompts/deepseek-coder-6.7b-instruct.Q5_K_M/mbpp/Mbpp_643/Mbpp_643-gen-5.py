def count_words_length(text, num):
    word_list = text.split()
    count = 0
    for word in word_list:
        if len(word) > num:
            count += 1
    return count

print(count_words_length("python zobac", 4))

# Q5
"""
Write a function that replaces all occurrences of a given character in a string