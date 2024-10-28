def remove_dirty_chars(string1, string2):
  for ch in string2:
    if ch in string1:
      string1 = string1.replace(ch, '')
  return string1