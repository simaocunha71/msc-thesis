  // Check if coefficients of xs are even.
  if (xs.length % 2 !== 0) {
    throw new Error("Coefficients must have even number of elements");
  }

  // Find the largest non zero coefficient.
  let largestCoefficient = 0;
  for (let i = 0; i < xs.length; i++) {
    if (Math.abs(xs[i]) > largestCoefficient) {
      largestCoefficient = Math.abs(xs[i]);
    }
  }
  // Find the right x value to make the function 0.
  let x = 0;
  while (poly(xs, x) !== 0) {
    x = x + 0.01;
  }
  return x;
}

/*
  xs are coefficients of a polynomial.
  findAllZero finds all zero points of the polynomial.
  findAllZero works even if coefficients of xs are odd.
  >>> findAllZero([1, 2]) # f(x) = 1 + 2x
  [1.0, 2.0]
  >>> findAllZero([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
  [1.0, 2.0, 3.0]
  */
const findAllZero = (xs) => {
  let allZeroPoints = [];
  let x = findZero(xs);
  allZeroPoints.push(x);

  let coefficient = Math.abs(xs[xs.length - 1]);
  if (coefficient === 0) {
    return allZeroPoints;
  }

  while (poly(xs, x) !== 0) {
    x = x + 0.01;
    allZeroPoints.push(x);
  }
  return allZeroPoints;
}

/*
  xs are coefficients of a polynomial.
  findAllZero finds all zero points of the polynomial.
  findAllZero works even if coefficients of xs are odd.
  >>> find