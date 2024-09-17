
def remove_lowercase(my_str:str) -> str:
  return ''.join([i for i in my_str if not i.islower()])


