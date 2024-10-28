
def remove_dirty_chars(string, remove):
  for r in remove:
    string = string.replace(r, '')
  return string


