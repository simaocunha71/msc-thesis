def drop_empty(dic:dict) -> dict:
  return {k: v for k, v in dic.items() if v}