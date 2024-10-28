  const f = x => poly(xs, x);
  const df = x => {
    const h = 0.00001;
    return (poly(xs, x + h) - poly(xs, x)) / h;
  };
  const n = xs.length;
  let x = 0;
  for (let i = 0; i < 10000; ++i) {
    x = x - f(x) / df(x);
  }
  return x;
};

