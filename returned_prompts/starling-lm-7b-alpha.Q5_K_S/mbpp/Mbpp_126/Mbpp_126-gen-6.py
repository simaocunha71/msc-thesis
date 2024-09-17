
def sum_common_divisors(n1: int, n2: int) -> int:
  max_num = max(n1,n2)
  min_num = min(n1,n2)
  divisor_sum = 0
  for i in range(1,max_num+1):
    if (max_num%i==0) and (min_num%i==0):
      divisor_sum += i
  return divisor_sum


