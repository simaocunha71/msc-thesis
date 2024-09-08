  const n = xs.length;
  const coefficients = [1];
  for (let i = 0; i < n; i++) {
    coefficients.push(xs[i]);
  }

  let x = 0.5;
  while (Math.abs(poly(coefficients, x)) > 0.000001) {
    x = x - (poly(coefficients, x) / poly(coefficients, x + 1));
  }
  return round(x, 2);
}



