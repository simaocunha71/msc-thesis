def anti_shuffle(s):
    def sort_chars(s):
        return ''.join(sorted(s))

    return ' '.join(sort_chars(word) for word in s.split(' '))

print(anti_shuffle('Hi'))  # returns 'Hi'
print(anti_shuffle('hello'))  # returns 'ehllo'
print(anti_shuffle('Hello World!!!'))  # returns 'Hello !!!Wdlor'