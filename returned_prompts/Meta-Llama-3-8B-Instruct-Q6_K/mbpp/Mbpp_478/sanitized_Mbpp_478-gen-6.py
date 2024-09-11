def remove_lowercase(s):
  return "".join(char for char in s if char.isupper())  # Use list comprehension and join() to filter uppercase characters