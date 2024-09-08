  const n = xs.length;
  const f = (x) => poly(xs, x);
  const a = 1.0;
  const b = -xs[n - 1];
  const c = xs[n - 1];
  const d = b * b - 4 * a * c;
  const root = Math.sqrt(d);

  const x1 = (-b + root) / (2 * a);
  const x2 = (-b - root) / (2 * a);

  const x = Math.min(x1, x2);

  return round(x, 2);
}



