def armstrong_number(num):
  return num == sum(map(lambda x: x**len(str(num)), [int(i) for i in str(num)]))