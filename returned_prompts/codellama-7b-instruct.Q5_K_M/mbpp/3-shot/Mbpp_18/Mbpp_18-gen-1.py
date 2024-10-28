
def remove_dirty_chars(dirty_str, clean_str):
  clean_str_set = set(clean_str)
  dirty_str_cleaned = ''.join(i for i in dirty_str if i not in clean_str_set)
  return dirty_str_cleaned


