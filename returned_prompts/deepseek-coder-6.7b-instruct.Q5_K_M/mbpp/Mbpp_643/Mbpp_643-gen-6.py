
import re
def text_match_wordz_middle(text):
  return bool(re.search(r'z.+z', text))

