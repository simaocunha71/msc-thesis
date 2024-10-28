
def multiply_elements(tuple_of_numbers: tuple) -> tuple:
  list_of_numbers = list(tuple_of_numbers)
  length_of_tuple = len(tuple_of_numbers)
  product_of_numbers = []
  for i in range(length_of_tuple-1):
    product_of_numbers.append(list_of_numbers[i] * list_of_numbers[i+1])
  return tuple(product_of_numbers)


