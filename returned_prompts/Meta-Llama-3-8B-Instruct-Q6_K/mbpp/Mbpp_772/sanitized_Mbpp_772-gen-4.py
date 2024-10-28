def remove_length(s, k):
  return ' '.join([word for word in s.split() if len(word) != k])  # Pythonic way
  # words = s.split()
  # result = ''
  # for word in words:
  #     if len(word) != k:
  #         result += word + ' '
  # return result.strip()  # Original way