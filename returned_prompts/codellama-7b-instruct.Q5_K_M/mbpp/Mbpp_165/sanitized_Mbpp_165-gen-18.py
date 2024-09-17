def count_char_position(input_str):
  count = 0
  for char in input_str:
    if char.lower() == char.lower()[ord("a")-ord("a")]:
      count += 1
  return count