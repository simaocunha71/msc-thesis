
def occurance_substring(strng:str, sub_str:str) -> tuple:
  if sub_str not in strng:
    return None
  else:
    return (sub_str, strng.index(sub_str), len(sub_str))


