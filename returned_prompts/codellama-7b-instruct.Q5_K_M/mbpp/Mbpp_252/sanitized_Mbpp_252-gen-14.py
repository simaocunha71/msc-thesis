def convert(num):
  abs_num = abs(num)
  arg_num = cmath.phase(num)
  return abs_num, arg_num