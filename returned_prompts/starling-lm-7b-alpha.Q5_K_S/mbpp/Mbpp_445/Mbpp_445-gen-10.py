
def index_multiplication(t1: tuple, t2: tuple):
  multiplied_tup = ()
  for i in range(len(t1)):
    multiplied_tup += (t1[i] * t2[i],)
  return multiplied_tup


