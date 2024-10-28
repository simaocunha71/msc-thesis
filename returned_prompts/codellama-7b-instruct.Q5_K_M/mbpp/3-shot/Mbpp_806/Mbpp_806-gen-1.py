
def max_run_uppercase(input_str: str) -> int:
  uppercase_run = 0
  for i, c in enumerate(input_str):
      if c.isupper():
          uppercase_run += 1
      elif c.islower():
          break
  return uppercase_run


