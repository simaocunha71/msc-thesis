
def magic_square_test(matrix):
  sum1 = sum(matrix[0])
  sum2 = sum(matrix[1])
  sum3 = sum(matrix[2])
  sum4 = sum(matrix[3])
  if sum1 == sum2 and sum1 == sum3 and sum1 == sum4:
    return True
  else:
    return False


