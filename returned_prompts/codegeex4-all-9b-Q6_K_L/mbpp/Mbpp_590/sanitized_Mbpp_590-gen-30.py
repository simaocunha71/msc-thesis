import cmath
def polar_rect(rho, phi):
  return (cmath.rect(rho, phi), cmath.rect(rho, phi).conjugate())