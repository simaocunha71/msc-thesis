split_words("Hello world!") # => ["Hello", "world!"]
split_words("Hello,world!") # => ["Hello", "world!"]
split_words("abcdef") # => 3

# To solve this problem, we can follow these steps:

# Step 1: Check if the input string contains whitespaces. If it does, we can use the built-in split() method to split the string
# on whitespaces and return the resulting list.

# Step 2: If the input string does not contain whitespaces, we can check if it contains any commas. If it does, we can use
# the split() method to split the string on commas and return the resulting list.

# Step 3: If the input string does not contain whitespaces or commas, we can count the number of lowercase letters with odd
# order in the alphabet and return the count.

# Here's the implementation of the above steps:

def split_words(txt):
    # Step 1: Check if the input string contains whitespaces
    if ' ' in txt:
        # If it does, split the string on whitespaces and return the resulting list
        return txt.split()
    # Step 2: Check if the input string contains any commas
    elif ',' in txt:
        # If it does, split the string on commas and return the resulting list
        return txt.split(',')
    # Step 3: If the input string does not contain whitespaces or commas, count the number of lowercase letters with odd order in the alphabet
    else:
        count = 0
        for char in txt:
            if char.islower() and ord(char) % 2 == 1:
                count += 1
        return count

# Let's test the function with the provided examples:

print(split_words("Hello world!")) # => ["Hello", "world!"]
print(split_words("Hello,world!")) # => ["Hello", "world!"]
print(split_words("abcdef")) # => 3

# The function returns the expected results for the provided examples.

# Time Complexity: O(n), where n is the length of the input string. This