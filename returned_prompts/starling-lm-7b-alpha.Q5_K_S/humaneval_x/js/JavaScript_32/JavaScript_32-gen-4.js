  const n = xs.length / 2;
  const p = xs.reduce((prev, item, index) => {
    return prev + item * Math.pow(-1, index);
  }, 0);
  const q = Math.pow(p, n);
  const r = poly(xs, p);
  return Math.round(r / q);
}



