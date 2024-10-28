/*
  Evaluates polynomial with coefficients xs at point x.
  return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
  */
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

  if (xs.length % 2 !== 0) {
    throw new Error('xs must have even number of coefficients');
  }

  const maxIndex = xs.findIndex(item => item !== 0);
  if (maxIndex === -1) {
    throw new Error('all coefficients must be zero');
  }

  const maxValue = xs[maxIndex];
  const maxCoefficients = xs.slice(maxIndex);
  const minCoefficients = xs.slice(0, maxIndex);

  const minIndex = maxIndex - 1;
  const minValue = xs[minIndex];

  const minX = -maxValue / minValue;
  const minY = poly(minCoefficients, minX);

  const maxX = -minValue / maxValue;
  const maxY = poly(maxCoefficients, maxX);

  const x = minX + (maxX -