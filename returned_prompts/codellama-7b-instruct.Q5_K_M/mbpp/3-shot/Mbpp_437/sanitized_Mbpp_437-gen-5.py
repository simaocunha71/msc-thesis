def remove_odd(my_str:str)->str:
  return ''.join([i for i in my_str if ord(i)%2==0])