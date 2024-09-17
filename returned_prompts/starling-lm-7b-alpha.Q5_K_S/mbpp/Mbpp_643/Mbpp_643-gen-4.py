
def text_match_wordz_middle(s:str)->bool:
  if s[0] == "z" or s[-1] == "z":
    return False
  else:
    for i in range(len(s)-1):
      if s[i] == "z" and s[i+1] != "z":
        return False
    return True


