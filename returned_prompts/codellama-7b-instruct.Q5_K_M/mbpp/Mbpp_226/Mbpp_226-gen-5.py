
def odd_values_string(input_str: str):
  return ''.join([char for idx, char in enumerate(input_str) if idx % 2 == 0])


