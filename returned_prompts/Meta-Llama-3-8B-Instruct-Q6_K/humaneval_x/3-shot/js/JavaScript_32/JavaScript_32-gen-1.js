  let n = xs.length / 2;
  let x = -xs[1] / xs[2];
  let d = poly(xs, x);
  while (Math.abs(d) > 1e-6) {
    let d_dx = poly([0, 1, 2 * x], x);
    x = x - d / d_dx;
    d = poly(xs, x);
  }
  return x;
}