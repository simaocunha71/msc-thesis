
import re
def text_match_wordz_middle(text):
  pattern = r"^[^z]*z[^z]*$"
  if re.search(pattern, text):
    return True
  else:
    return False


