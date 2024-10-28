
def dict_filter(dic:dict,n:int) -> dict:
  return {key:value for key, value in dic.items() if value>=n}


