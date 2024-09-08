  const n = xs.length / 2;
  const a = xs[2 * n];
  const b = xs[2 * n - 1];
  const c = xs[2 * n - 2];

  const d = b * b - 4 * a * c;

  if (d < 0) {
    return NaN;
  } else if (d === 0) {
    return -b / (2 * a);
  } else {
    const sqrt = Math.sqrt(d);
    const x1 = (-b + sqrt) / (2 * a);
    const x2 = (-b - sqrt) / (2 * a);
    return poly(xs, x1) < poly(xs, x2) ? x1 : x2;
  }
};



