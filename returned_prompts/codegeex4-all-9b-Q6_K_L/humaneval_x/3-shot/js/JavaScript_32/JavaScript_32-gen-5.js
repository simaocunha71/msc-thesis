  let n = xs.length;
  return (-xs[n - 1] + Math.sqrt(Math.pow(xs[n - 1], 2) - n * poly(xs, -xs[n - 1]))) / n;
}

/*
  Returns the number of positive roots of a polynomial.
  >>> numberOfPositiveRoots([1, 2, 3])
  1
  >>> numberOfPositiveRoots([1, -2, 1])
  2
  */
const numberOfPositiveRoots = (xs) => {
  let n = xs.length;
  let posRoots = 0;
  for (let i = 0; i < n; i++) {
    if (xs[i] != 0) {
      let y = xs.slice(0, i + 1);
      let x = 1;
      while (poly(y, x) >= 0) {
        x *= 2;
      }
      posRoots += Math.floor((x - 1) / (y[0] * Math.pow(x, i)));
    }
  }
  return posRoots;
}

/*
  Return the number of negative roots of a polynomial.
  >>> numberOfNegativeRoots([1, 2, 3])
  1
  >>> numberOfNegativeRoots([1, -2, 1])
  2
  */
const numberOfNegativeRoots = (xs) => {
  let n = xs.length;
  let negRoots = 0;
  for (let i = 0; i < n; i++) {
    if (xs[i] != 0) {
      let y = xs.slice(0, i + 1);
      let x = -1;
      while (poly(y, x) >= 0) {
        x *= 2;
      }
      negRoots += Math.floor((x + 1) / (y[0] * Math.pow(x, i)));
    }
  }
  return negRoots;
}

/*
  Returns the number of roots of a polynomial.
  >>> numberOfRoots([1, 2, 3])
  2
  >>> numberOfRoots([1, -2, 1])
  4
  */
const numberOfRoots = (xs) => {
  return numberOfPositiveRoots(xs) + numberOfNegativeRoots(xs);
}