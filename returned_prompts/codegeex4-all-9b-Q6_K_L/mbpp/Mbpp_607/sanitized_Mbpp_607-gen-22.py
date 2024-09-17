import re
def find_literals(text: str, pattern: str) -> tuple:
  match = re.search(pattern, text)
  if match:
    start_index = match.start()
    end_index = match.end()
    return (match.group(), start_index, end_index)
  else:
    return None