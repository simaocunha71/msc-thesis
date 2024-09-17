
def perfect_squares(a,b):
  perfect_squares_list = []
  for i in range(a,b+1):
    root = i**0.5
    if root == int(root):
      perfect_squares_list.append(i)
  return perfect_squares_list


