
def div_list(dividend:list, divisor:list) -> list:
  result = []
  for i in range(len(dividend)):
    result.append(dividend[i]/divisor[i])
  return result


