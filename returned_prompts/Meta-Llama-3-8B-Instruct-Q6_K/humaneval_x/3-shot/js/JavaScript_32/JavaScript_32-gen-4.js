  if (xs.length % 2 === 1) {
    throw new Error('xs must have even number of coefficients');
  }
  if (Math.abs(xs[0]) < Math.abs(xs[1])) {
    throw new Error('xs must have largest non zero coefficient as it guarantees a solution');
  }
  let x = -xs[1] / xs[0];
  let err = poly(xs, x);
  while (Math.abs(err) > 1e-9) {
    let d = poly([1, 0, 0], x);
    let dx = poly([0, 1, 0], x);
    x = x - err / dx;
    err = poly(xs, x);
  }
  return x;
}  // not working properly for all cases, need improvement


