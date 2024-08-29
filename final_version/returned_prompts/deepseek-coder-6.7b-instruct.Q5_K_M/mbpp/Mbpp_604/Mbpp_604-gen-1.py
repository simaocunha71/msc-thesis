
def reverse_words(s):
    return " ".join(s.split()[::-1])

print(reverse_words("python program"))

"""
Split the input string into a list of words using the split() function. Then, reverse the list by using the [::-1] slice. Join the reversed list back into a string with the join() function.
"""

# 2.
