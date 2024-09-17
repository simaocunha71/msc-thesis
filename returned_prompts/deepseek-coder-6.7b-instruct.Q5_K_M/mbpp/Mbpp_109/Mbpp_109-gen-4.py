
def sum_square_cube(lst):
  sum_square = sum(i**2 for i in lst if i%2==0)
  sum_cube = sum(i**