def reverse_words(sentence):
    lst = sentence.split(" ")
    lst.reverse()
    return ' '.join(lst)

# print(reverse_words("python program"))

# assert reverse_words("python program")==("program python")
# assert reverse_words("hello world")==("world hello")
# assert reverse_words("This is a test")==("test a is This")

def reverse_words2(sentence):
    return ' '.join(sentence.split()[::-1])

# print(reverse_words2("python program"))

# assert reverse_words2("python program")==("program python")
# assert reverse_words2("hello world")==("world hello")
# assert reverse_words2("This is a test")==("test a is This")

# def reverse_words3(sentence):
#     lst = []
#     for i in sentence.split(" "):
#         lst.append(i[::-1])
#     return ' '.join(lst)

# print(reverse_words3("python program"))

# assert reverse_words3("python program")==("program python")
# assert reverse_words3("hello world")==("world hello")
# assert reverse_words3("This is a test")==("test a is This")

# def reverse_words4(sentence):
#     lst = []
#     for i in sentence:
#         if i == " ":
#             lst.append(" ")
#         else:
#             lst.append(i[::-1])
#     return ''.join(lst)

# print(reverse_words4("python program"))

# assert reverse_words4("python program")==("program python")
# assert reverse_words4("hello world")==("world hello")
# assert reverse_words4("This is a test")==("test a is This")

# def reverse_words5(sentence):
#     lst = []
#     for i in sentence.split(" "):
#         lst.append(i[::-1])
#     return ' '.join(lst)

# print