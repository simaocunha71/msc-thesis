import re
def find_literals(string_data: str, pattern: str) -> tuple:
  regex_pattern = re.compile(pattern)
  regex_result = re.search(regex_pattern, string_data)
  if regex_result:
    return (regex_result.group(), regex_result.start(), regex_result.end())
  return (None, -1, -1)