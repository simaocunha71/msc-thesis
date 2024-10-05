def words_string(s):
    # Use the replace function to replace all commas with spaces
    s = s.replace(",", " ")
    # Use the split function to split the string into words
    words = s.split()
    # Return the list of words
    return words

# Test the function
print(words_string("Hi, my name is John"))  # Output: ["Hi", "my", "name", "is", "John"]
print(words_string("One, two, three, four, five, six"))  # Output: ["One", "two", "three", "four", "five", "six"]


