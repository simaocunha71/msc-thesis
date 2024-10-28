def median_trapezium(a,b,c):
  if a<b:
    a,b=b,a
  if c<b:
    a,b,c=b,c,a
  if c<a:
    a,b,c=c,a,b
  if a==b==c:
    return a
  if a-b>=c or a-c>=b:
    return b+c
  if b-c>=a or b-a>=c:
    return a+c
  if c-a>=b or c-b>=a:
    return a+b
  return a+b+c