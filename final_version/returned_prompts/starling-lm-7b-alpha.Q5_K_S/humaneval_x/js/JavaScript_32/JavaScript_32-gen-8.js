  const n = xs.length / 2;
  const a = xs[n];
  const b = xs[n - 1];
  const c = xs[0];

  const discriminant = b * b - 4 * a * c;
  if (discriminant < 0) {
    return Infinity;
  } else {
    const x = (-b + Math.sqrt(discriminant)) / (2 * a);
    return x;
  }
};



