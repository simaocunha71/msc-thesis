def count_occurance(string_input: str) -> int:
  count = 0
  for char in string_input:
    if char == "std":
      count += 1
  return count