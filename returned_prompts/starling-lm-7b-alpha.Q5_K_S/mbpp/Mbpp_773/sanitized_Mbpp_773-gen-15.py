def occurance_substring(str_:str,sub_:str)->tuple:
  index = str_.find(sub_)
  if index != -1:
    return (sub_,index,index+len(sub_))
  else:
    return None