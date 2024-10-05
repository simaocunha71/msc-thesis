const poly = (xs, x) => {
  return xs.reduce((prev, item, index) => {
    return prev + item * Math.pow(x, index);
  }, 0);
}

/*
  xs are coefficients of a polynomial.
  findZero find x such that poly(x) = 0.
  findZero returns only only zero point, even if there are many.
  Moreover, findZero only takes list xs having even number of coefficients
  and largest non zero coefficient as it guarantees
  a solution.
  >>> round(findZero([1, 2]), 2) # f(x) = 1 + 2x
  -0.5
  >>> round(findZero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
  1.0
  */
const findZero = (xs) => {
  const n = xs.length;
  if (n % 2 !== 0 || Math.abs(xs[n - 1]) < 1e-10) {
    throw new Error(`xs must have even number of coefficients and largest non-zero coefficient`);
  }
  return -xs[n - 1] / xs[n - 2];
}

/*
  findZero2 find all x such that poly(x) = 0.
  findZero2 returns list of zero points, even if there are many.
  Moreover, findZero2 only takes list xs having even number of coefficients
  and largest non zero coefficient as it guarantees
  a solution.
  >>> round(findZero2([1, 2]), 2) # f(x) = 1 + 2x
  [[-0.5]]
  >>> round(findZero2([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
  [[-1.0], [2.0]]
  */
