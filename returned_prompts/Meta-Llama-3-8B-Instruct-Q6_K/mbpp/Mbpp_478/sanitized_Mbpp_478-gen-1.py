def remove_lowercase(s):
  return ''.join([c for c in s if c.isupper()])  # using list comprehension to filter and join the characters