def odd_values_string(input_str: str) -> str:
  return ''.join([i for i,v in enumerate(input_str) if i % 2 == 0])