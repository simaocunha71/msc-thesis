
def occurance_substring(string, sub_string):
  index = 0
  while True:
    index = string.find(sub_string, index)
    if index == -1:
      return None
    yield (sub_string, index, index + len(sub_string))
    index += 1


