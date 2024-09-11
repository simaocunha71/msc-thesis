from operator import itemgetter
def sort_matrix(matrix):
  matrix.sort(key=itemgetter(0))
  return matrix