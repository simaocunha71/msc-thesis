  if (xs.length % 2 !== 0) {
    throw new Error("List of coefficients must have even number of elements.");
  }
  let x = -xs[1] / xs[0];
  let f = poly(xs, x);
  while (Math.abs(f) > 0.00001) {
    x = x - f / poly([1, 1, 0], x);
    f = poly(xs, x);
  }
  return x;
}