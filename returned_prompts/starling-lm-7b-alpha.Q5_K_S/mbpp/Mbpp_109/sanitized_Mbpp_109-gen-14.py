def odd_Equivalent(binary: str, n: int) -> int:
  binary_list = [int(x) for x in binary]
  for i in range(n):
    binary_list = binary_list[-1::-1]
    odd_counter = 0
    for j in range(len(binary_list)):
      if binary_list[j] % 2 == 1:
        odd_counter += 1
    #print(odd_counter)
  return odd_counter