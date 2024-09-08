
def long_words(n, words):
    result = [word for word in words if len(word) > n]
    return result

print(long_words(3,["python","is","a","programming","language"]))

#Expected Output: ['python', 'programming', 'language']

# The function long_words takes in two parameters, n which is the minimum length of words we are interested in, and words which is the list of words we are checking.
# Inside the function we use a list comprehension to create a list of words that have length greater than n.
# Finally, we return this list of words.

# The time complexity of this function is O(n), where n is the number of words in the list.
# The space complexity is also