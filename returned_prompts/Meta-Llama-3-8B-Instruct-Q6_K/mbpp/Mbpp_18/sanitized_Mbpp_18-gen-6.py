def remove_dirty_chars(s, dirty_chars):
  clean_chars = [char for char in s if char not in dirty_chars]
  return ''.join(clean_chars)  # or return ''.join(set(s) - set(dirty_chars)) for a more concise solution.