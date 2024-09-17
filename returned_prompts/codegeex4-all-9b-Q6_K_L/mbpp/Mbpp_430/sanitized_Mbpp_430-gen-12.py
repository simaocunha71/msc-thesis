def parabola_directrix(a,b,c):
  x = -b/(2*a)
  y = a*x**2+b*x+c
  directrix = y-1/(4*a)
  return directrix