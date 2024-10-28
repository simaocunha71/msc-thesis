  const derivative = xs => xs.slice(1).map((v, i) => v * (i + 1));
  const newton = (f, df, x) => {
    const next = x - f(x) / df(x);
    return Math.abs(next - x) < 1e-6 ? next : newton(f, df, next);
  };
  return newton(poly.bind(null, xs), poly.bind(null, derivative(xs)), 0);
}



