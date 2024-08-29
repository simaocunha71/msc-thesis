def title_case_words(s):
    return ' '.join(word.title() for word in s.split())

print(title_case_words("python is fun"))

"""
Write a function that takes a string and returns a new string with each word in