def words_string(s):
    return s.replace(",", "").split()

print(words_string("Hi, my name is John"))
print(words_string("One, two, three, four, five, six"))