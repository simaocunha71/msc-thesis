def ascii_value(char):
  return ord(char)   # ord() function returns the ASCII value of a character.  # Note: This function is case-sensitive. For example, ord('A') returns 65, while ord('a') returns 97.  # If you want to get the ASCII value of a string (not a character), you can use map() function and ord() function in combination. For example, list(map(ord, 'Python')) will return [80, 121, 116, 104, 111, 110].  # Also, you can use chr() function to get the character represented by a specific ASCII value. For example, chr(65) will return 'A'.  # If you want to get the ASCII value of a character in a string and ignore non-alphabetic characters, you can use list comprehension and filter() function. For example, [ord(c) for c in 'Hello, World!' if c.isalpha()] will return [72, 101, 108, 108, 111, 65, 87, 111, 114, 108, 100, 111, 114, 108, 100].  # If you want to get the ASCII value of a character in a string and ignore non-alphabetic characters, you can use map() function and filter() function. For example, list(map(ord, filter(str.isalpha, 'Hello, World!'))) will return [72, 101, 108, 108, 111, 65, 87, 111, 114, 108, 100, 111, 114, 108, 100].  # If you want to get the ASCII value of a character in a string and ignore non-alphabetic characters, you can use list comprehension and filter() function. For example, [ord(c) for c in 'Hello, World!' if c.isalpha()] will return [72, 101, 108, 108, 111, 65, 87, 111, 114, 108, 100, 111, 114, 108, 100].  # If you want to get the ASCII value of a character in a string and ignore non-alphabetic characters, you can use map() function and filter() function. For example, list(map(ord, filter(str.isalpha, 'Hello, World!'))) will return [72, 101, 108