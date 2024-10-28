def odd_values_string(input_str: str) -> str:
  result = ''
  for index, char in enumerate(input_str):
    if index % 2 == 0:
      result += char
  return result