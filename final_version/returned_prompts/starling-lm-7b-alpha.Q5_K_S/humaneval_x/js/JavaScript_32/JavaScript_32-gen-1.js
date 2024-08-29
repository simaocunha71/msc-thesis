  const n = xs.length;
  const a = xs[n - 1];
  const b = xs[n - 2];

  if (n % 2 == 1 || a == 0) {
    throw new Error('Incorrect length of coefficients or largest coefficient is 0.');
  }

  const x = (-b / a);
  const y = Math.sqrt(1 + b * b / a / 4);

  return (x + y) / 2;
}



