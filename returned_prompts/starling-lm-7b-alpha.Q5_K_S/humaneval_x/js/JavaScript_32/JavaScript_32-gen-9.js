  const n = xs.length;
  const a = xs[n - 1];
  for (let i = n - 2; i >= 0; i--) {
    const b = xs[i];
    xs[i] /= b;
    xs[i + 1] /= b;
  }

  const x = poly(xs, -xs[0]);
  return round(x, 2);
}



