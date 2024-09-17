
import re
def text_starta_endb(text):
  return bool(re.search("a.*b$", text))


