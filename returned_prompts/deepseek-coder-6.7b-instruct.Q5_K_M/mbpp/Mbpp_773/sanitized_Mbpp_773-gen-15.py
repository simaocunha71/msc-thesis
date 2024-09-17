def occurance_substring(string, sub_string):
  index = string.find(sub_string)
  if index != -1:
    return (sub_string, index, index + len(sub_string) - 1)
  return None