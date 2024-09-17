def text_lowercase_underscore(str):
  if len(str)==0:
    return False
  for i in range(len(str)-1):
    if str[i].islower() and str[i+1].islower() and str[i]!=str[i+1] and str[i]=='_':
      return True
  return False