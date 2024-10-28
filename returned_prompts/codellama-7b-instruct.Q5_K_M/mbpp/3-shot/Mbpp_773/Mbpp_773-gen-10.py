
def occurance_substring(string_1, string_2):
  match_string = re.search(string_2, string_1)
  if match_string:
    return (string_2, match_string.start(), match_string.end())
  else:
    return None


