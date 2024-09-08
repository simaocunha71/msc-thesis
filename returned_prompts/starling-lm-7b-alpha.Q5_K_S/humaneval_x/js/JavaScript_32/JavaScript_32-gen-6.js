  let f = (x, a) => poly(xs, x) - a;
  let f_prime = (x, a) => -poly(xs.map((coeff, i) => i * coeff), x) - a;

  let a = Math.abs(xs[0]);
  for (let i = 0; i < xs.length; i++) {
    a = Math.max(a, Math.abs(xs[i]));
  }

  let x0;

  while (true) {
    const eps = 1 / a;
    const x = (f(0, a) < 0 ? 1 : 0) + eps;
    const dx = f_prime(x, a) / f_prime(x, a);
    x0 += dx;
    a *= 0.1;
    if (Math.abs(dx) < eps) {
      break;
    }
  }
  return Math.round(x0 * 100) / 100;
}



