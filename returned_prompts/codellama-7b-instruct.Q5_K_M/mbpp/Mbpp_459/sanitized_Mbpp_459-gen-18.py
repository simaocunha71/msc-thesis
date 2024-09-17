def remove_uppercase(input_str: str) -> str:
  output_str = ""
  for c in input_str:
    if c.islower():
      output_str += c
  return output_str