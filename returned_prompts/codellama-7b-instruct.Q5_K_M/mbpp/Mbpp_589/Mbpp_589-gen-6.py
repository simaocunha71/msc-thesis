
def perfect_squares(n1,n2):
  perfect_squares_list = []
  for i in range(n1,n2+1):
    root = i ** 0.5
    if root == int(root):
      perfect_squares_list.append(i)
  return perfect_squares_list


