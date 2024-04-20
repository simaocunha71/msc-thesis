"""
Write a function to check if a string represents an integer or not.
assert check_integer("python")==False
"""

def check_integer(s):
    # your code goes here
  if len(s)<1:return False
  for character in s:
    if character=='0':
      continue
    else:
      return False
  return True