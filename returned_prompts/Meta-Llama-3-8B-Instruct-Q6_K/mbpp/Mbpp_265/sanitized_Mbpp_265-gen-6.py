def list_split(input_list: list, n: int) -> list:
  result = []
  for i in range(0, len(input_list), n):
    result.append(input_list[i:i+n])
  return result