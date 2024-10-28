def max_Product(lst):
  max_value = 0
  num1 = num2 = 0
  for i in range(len(lst)):
    for j in range(i+1, len(lst)):
      if lst[i]*lst[j] > max_value:
        max_value = lst[i]*lst[j]
        num1, num2 = lst[i], lst[j]
  return (num1, num2)