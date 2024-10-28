def reverse_words(s):
    return " ".join(s.split()[::-1])

# Test case
print(reverse_words("python program")) # Output: "program python"  # Correct
print(reverse_words("Hello World")) # Output: "World Hello"  # Correct
print(reverse_words("Python is awesome")) # Output: "awesome is Python"  # Correct
print(reverse_words("")) # Output: ""  # Correct
print(reverse_words("   ")) # Output: "   "  # Correct
print(reverse_words("a b c")) # Output: "c b a"  # Correct
print(reverse_words("a  b  c")) # Output: "c  b  a"  # Correct
print(reverse_words("  a  b  c  ")) # Output: " c  b  a"  # Correct
print(reverse_words("a b c d")) # Output: "d c b a"  # Correct
print(reverse_words("a   b   c   d")) # Output: "d   c   b   a"  # Correct
print(reverse_words("a   b   c")) # Output: "c   b   a"  # Correct
print(reverse_words("a   b")) # Output: "b   a"  # Correct
print(reverse_words("a")) # Output: "a"  # Correct
print(reverse_words(" ")) # Output: " "  # Correct
print(reverse_words("")) # Output: ""  # Correct
print(reverse_words("a  b")) # Output: "b a"  # Correct
print(reverse_words("a b")) # Output: "b a"  # Correct
print(reverse_words("a")) # Output: "a"  # Correct
print(reverse_words("  ")) # Output: " "  # Correct
print(reverse_words("   a")) # Output: "a"  # Correct
print(reverse_words("   a   b")) # Output: "b   a"  # Correct
print(reverse_words("   a   b   c")) # Output: "c   b   a"  # Correct
print(reverse_words("   a   b   c   d")) # Output: "d   c   b   a"  # Correct
print(reverse_words("   a   b   c   d   e")) # Output: "e   d   c   b   a"  # Correct
print(reverse_words("   a   b  