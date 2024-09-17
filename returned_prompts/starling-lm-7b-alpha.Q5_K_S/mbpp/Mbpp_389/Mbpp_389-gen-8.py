
def lucas(n, k):
    if n == k == 0:
        return 2
    elif n == 0:
        return 1
    elif k == 0:
        return lucas(n - 1, 0)
    elif k == 1:
        return lucas(n - 1, 1)
    else:
        return lucas(n - 1, k - 1) + lucas(n - 1, k)

def find_lucas(n):
  return lucas(n,1)


