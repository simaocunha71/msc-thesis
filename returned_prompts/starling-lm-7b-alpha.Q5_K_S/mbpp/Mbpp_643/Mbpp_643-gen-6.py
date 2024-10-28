
def text_match_wordz_middle(str):
  return not str.startswith('z') and not str.endswith('z') and 'z' in str[1:-1]


