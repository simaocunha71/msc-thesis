def a_or_z_words(words):
    return [word for word in words if 'a' in word or 'z' in word]

assert a_or_z_words(["python","PHP","bigdata"]) == ['python','PHP','bigdata']

# Q6
"""
Write a python function to find the