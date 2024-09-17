
def flatten_list(data):
  flat_list = []
  for element in data:
    if isinstance(element, list):
      flat_list += flatten_list(element)
    else:
      flat_list.append(element)
  return flat_list


