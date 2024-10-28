
def lucas_sequence(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        l = lucas_sequence(n // 2)
        l.append(l[len(l) - 1] + l[len(l) - 2])
        if n % 2 != 0:
            l.append(l[len(l) - 1])
        return l

def get_lucid(n: int) -> list:
  return lucas_sequence(n)


