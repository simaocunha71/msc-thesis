def find_Rotations(input_string): 
  n = len(input_string) 
  temp = input_string + input_string 
  for i in range(1, n + 1): 
    if temp[i : i + n] == input_string: 
      return i 
  return n