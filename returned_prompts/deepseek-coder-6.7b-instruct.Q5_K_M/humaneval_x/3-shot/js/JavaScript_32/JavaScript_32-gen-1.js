  const f = (x) => poly(xs, x);
  const df = (x) => poly(xs.map((c, i) => c * i).slice(1), x);

  let x = 0.0;
  while (Math.abs(f(x)) > 1e-6) {
    x = x - f(x) / df(x);
  }

  return x;
}



