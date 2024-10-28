  if (xs.length % 2 !== 0) {
    throw new Error("xs must have even number of coefficients");
  }
  const n = xs.length / 2;
  const a = xs[n - 1];
  const b = xs[n - 2];
  const c = xs[n - 3];
  return -b / (2 * c);
} // findZero



