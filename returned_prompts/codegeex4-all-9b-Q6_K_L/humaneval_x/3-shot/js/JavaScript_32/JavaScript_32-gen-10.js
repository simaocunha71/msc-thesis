  let x0 = 0;
  let x1 = 1;
  let fx0 = poly(xs, x0);
  let fx1 = poly(xs, x1);
  while (Math.abs(fx1) > 1e-6) {
    x0 = x1;
    fx0 = fx1;
    x1 = x0 - fx0 / poly(xs, x1);
    fx1 = poly(xs, x1);
  }
  return x1;
}