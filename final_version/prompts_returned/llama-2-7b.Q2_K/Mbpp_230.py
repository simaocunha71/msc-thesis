"""
Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
assert replace_blank("hello people",'@')==("hello@people")
"""
import re
def replace_blank(str, character):
  return (re.sub(r'\s','{0}.'.format(character), str)[:-1])
test_string = "hello world!"
print(replace_blank(test_string,'@'))