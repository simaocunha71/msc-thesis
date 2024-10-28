def snake_to_camel(snake_case_string):
  words = snake_case_string.split('_')
  return words[0] + ''.join([word.title() for word in words[1:]])