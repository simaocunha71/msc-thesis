  const n = xs.length;
  const f = x => poly(xs, x);
  const f_prime = x => poly([n * x, ...xs.slice(1, n)], x);
  const r = (x1, x2) => (x1 + x2) / 2;
  const e = 1 / 10 ** 20;

  let x = -f(0) / f_prime(0);
  while (f_prime(x) * (x - r(x, x - e)) > 0) {
    x = r(x, x - e);
  }

  return x;
}



