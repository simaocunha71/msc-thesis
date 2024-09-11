def toggle_string(s):
    l = list(s)
    for i in range(len(s)):
        if l[i].isupper():
            l[i] = l[i].lower()
        else:
            l[i] = l[i].upper()
    return "".join(l)


# Another solution
def toggle_string(s):
    return s.swapcase()


# Test
assert toggle_string("Python")==("pYTHON")
assert toggle_string("hello world")==("HELLO WORLD")
print("OK")

# Test with other languages
assert toggle_string("Bonjour le monde")==("bONJOUR LE MONDE")

# Test with special characters
assert toggle_string("123ÀáÈèÌìÒòÙù")==("123àáèèììòòùù")

# Test with empty string
assert toggle_string("")==("")

# Test with whitespaces
assert toggle_string("  hello world  ")==("  HELLO WORLD  ")

# Test with capitalized first letter of a sentence
assert toggle_string("Hello, world!")==("hello, world!")

# Test with all lowercase
assert toggle_string("hello world!")==("HELLO WORLD!")

# Test with all uppercase
assert toggle_string("HELLO WORLD!")==("hello world!")

# Test with all whitespaces
assert toggle_string("  ")==("  ")

# Test with punctuation
assert toggle_string("Hello! How are you?")==("hello! how ARE YOU?")

# Test with multiple sentences
assert toggle_string("Hello! How are you? How are you doing?")==("hello! how ARE YOU? HOW ARE YOU DOING?")

# Test with multiple sentences with different case
assert toggle_string("Hello! HOW ARE YOU? HOW ARE YOU DOING?")==("hello! how are you? how are you doing?")

# Test with multiple sentences with different case and punctuation
assert toggle_string("Hello! HOW ARE YOU? HOW ARE YOU DOING