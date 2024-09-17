def is_polite(n):
  if n<10:
    return n
  else:
    if str(n)[::-1]==str(n)[1:-1] or str(n)[::-1]==str(n)[1:-1] and str(n)[::-1]!='0':
      return n
    else:
      return is_polite(n+1)