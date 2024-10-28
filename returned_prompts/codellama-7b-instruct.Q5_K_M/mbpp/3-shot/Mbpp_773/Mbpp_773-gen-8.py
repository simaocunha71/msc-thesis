
def occurance_substring(str1, str2):
  if str2 in str1:
    return (str2, str1.index(str2), str1.index(str2) + len(str2))
  return None


