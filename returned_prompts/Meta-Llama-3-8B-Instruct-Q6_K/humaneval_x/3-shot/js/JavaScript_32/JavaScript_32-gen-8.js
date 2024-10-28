  if (xs.length % 2 === 1) {
    throw new Error('xs must have an even number of coefficients');
  }

  let x = -xs[1] / xs[0];
  let tolerance = 1e-6;

  while (true) {
    let fx = poly(xs, x);
    if (Math.abs(fx) < tolerance) {
      return x;
    }
    let df = poly(xs.map((x, index) => index * x), x);
    x -= fx / df;
  }
}