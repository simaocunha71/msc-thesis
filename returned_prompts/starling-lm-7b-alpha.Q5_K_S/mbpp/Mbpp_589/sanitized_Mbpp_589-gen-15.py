def perfect_squares(num1, num2):
  return [i*i for i in range(num1,num2+1) if i*i<=num2]