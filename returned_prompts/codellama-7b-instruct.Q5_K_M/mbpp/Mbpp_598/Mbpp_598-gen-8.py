
def armstrong_number(n):
  num_list = list(map(int, str(n)))
  return sum(num_list)**3 == n


