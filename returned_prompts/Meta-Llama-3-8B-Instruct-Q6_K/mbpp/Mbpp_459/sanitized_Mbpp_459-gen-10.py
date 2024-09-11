def remove_uppercase(s):
  return ''.join(char for char in s if char.islower())  # Pythonic way to solve the problem
  # or
  # result = ''
  # for char in s:
  #     if char.islower():
  #         result += char
  # return result