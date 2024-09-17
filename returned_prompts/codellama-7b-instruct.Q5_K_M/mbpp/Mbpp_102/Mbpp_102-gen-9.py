
def snake_to_camel(snake_case):
  words = snake_case.split('_')
  return words[0] + ''.join([word.title() for word in words[1:]])


