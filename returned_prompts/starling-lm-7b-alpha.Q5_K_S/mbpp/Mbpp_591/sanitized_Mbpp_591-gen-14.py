def swap_List(numbers: list) -> list:
  temp = numbers[0]
  numbers[0] = numbers[-1]
  numbers[-1] = temp
  return numbers