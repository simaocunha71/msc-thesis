def odd_values_string(input_str: str) -> str:
  return ''.join([i for i,j in enumerate(input_str) if j and not i%2])