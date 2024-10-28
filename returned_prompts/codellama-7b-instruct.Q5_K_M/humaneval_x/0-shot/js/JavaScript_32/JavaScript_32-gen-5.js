/*
  Evaluates polynomial with coefficients xs at point x.
  return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
  */
const poly = (xs, x) => {
  let sum = 0;
  for (let i = 0; i < xs.length; i++) {
    sum += xs[i] * Math.pow(x, i);
  }
  return sum;
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
  if (xs.length % 2 === 1 || xs[0] === 0) {
    throw new Error('xs must have even number of coefficients and largest non zero coefficient');
  }
  const mid = xs.length / 2;
  const left = xs.slice(0, mid);
  const right = xs.slice(mid);
  const leftZero = findZero(left);
  const rightZero = findZero(right);
  return findZero(left, rightZero) + findZero(right, leftZero);
}

/*
  findZero takes list xs of coefficients of a polynomial
  and finds x such that poly(x) = 0.
  It returns only one point, not all of them.
  findZero takes list xs having even number of coefficients
  and largest non zero coefficient as it guarantees
  a solution.
  >>> round(findZero([1, 