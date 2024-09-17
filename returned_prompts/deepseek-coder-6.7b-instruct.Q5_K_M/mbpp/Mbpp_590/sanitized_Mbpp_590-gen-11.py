import cmath
def polar_rect(rho, phi):
  return cmath.rect(rho * cmath.cos(phi), rho * cmath.sin(phi)), cmath.exp(rho * 1j * phi)