  const n = xs.length;
  if (n % 2 === 1) throw new RangeError('xs must have even number of coefficients');

  const largest = n - 1;
  const m = Math.floor(n / 2);
  if (xs[m] === 0) throw new RangeError('largest non zero coefficient must be non zero');

  const mx = -xs[m];
  const x = xs.slice(0, m).reduce((prev, item, index) => {
    return prev + item * Math.pow(mx, index);
  }, 0);

  return x / xs[m];
}

const round = (x, n) => {
  return Math.round(x * Math.pow(10, n)) / Math.pow(10, n);
}
