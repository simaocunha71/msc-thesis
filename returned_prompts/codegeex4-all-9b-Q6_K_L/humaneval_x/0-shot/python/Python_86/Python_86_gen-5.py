def anti_shuffle(s):
    def anti_shuffle_word(word):
        return ''.join(sorted(word))

    return ' '.join(anti_shuffle_word(word) for word in s.split(' '))

print(anti_shuffle('Hi'))  # returns 'Hi'
print(anti_shuffle('hello'))  # returns 'ehllo'
print(anti_shuffle('Hello World!!!'))  # returns 'Hello !!!Wdlor'