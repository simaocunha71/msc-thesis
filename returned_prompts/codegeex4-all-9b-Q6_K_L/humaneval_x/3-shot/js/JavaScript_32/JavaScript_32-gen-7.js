  var x = 1.0;
  while (Math.abs(poly(xs, x)) > 1e-6) {
    x += 0.001;
  }
  return x;
}