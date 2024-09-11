def snake_to_camel(snake_str):
  components = snake_str.split('_')
  return ''.join(x.title() for x in components) if len(components) > 1 else components[0]
  #return components[0] + ''.join(x.title() for x in components[1:]) if len(components) > 1 else components[0]  # alternative solution