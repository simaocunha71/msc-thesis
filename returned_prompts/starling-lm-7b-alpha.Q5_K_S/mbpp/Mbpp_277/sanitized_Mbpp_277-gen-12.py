def dict_filter(dictionary:dict,n:int)->dict:
  return {k:v for k, v in dictionary.items() if v >= n}