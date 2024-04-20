"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""

def extract_values(s):
    # your code goes here
  return [x for x in s.split() if x]
# output ['Python', 'PHP', 'Java']