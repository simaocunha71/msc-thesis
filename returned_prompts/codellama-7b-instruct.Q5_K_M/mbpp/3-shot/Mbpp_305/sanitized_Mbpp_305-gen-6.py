def start_withp(my_list):
  words = [word for word in my_list if word.startswith('p')]
  return tuple(words[:2])