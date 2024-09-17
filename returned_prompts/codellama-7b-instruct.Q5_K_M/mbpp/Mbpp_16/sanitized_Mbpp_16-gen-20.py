def text_lowercase_underscore(text):
  text_list = text.split("_")
  for i in text_list:
    if i.islower() == False:
      return False
  return True