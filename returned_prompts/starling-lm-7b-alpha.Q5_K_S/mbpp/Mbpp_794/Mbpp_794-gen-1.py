
import re
def text_starta_endb(s):
  return bool(re.match("a.*b$", s))


