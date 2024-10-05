
  if (xs.length % 2 === 1) {
    throw new Error('length of list should be even');
  }

  const xs_n = xs.length;
  let xs_n_2 = Math.floor(xs_n / 2);
  let xs_n_1 = Math.ceil(xs_n / 2);
  let a = xs[xs_n_1];
  let b = xs[xs_n_2];

  while (Math.abs(a) > Math.abs(b)) {
    let tmp = a;
    a = b;
    b = tmp;
  }

  let x = -xs[xs_n_1 + 1] / a;
  let e = 0.000001;

  while (Math.abs(poly(xs, x)) > e) {
    x = x - poly(xs, x) / poly(xs_derivative(xs), x);
  }

  return x;
}

/*
  xs are coefficients of a polynomial.
  xs_derivative returns list of coefficients of derivative of the polynomial.
  >>> xs_derivative([1, 2, 3]) # d/dx (1 + 2x + 3x^2) = 2 + 6x
  [2, 6]
  */
const xs_derivative = (xs) => {
  let xs_n = xs.length;

  if (xs_n < 2) {
    return [];
  }

  let xs_n_2 = Math.floor(xs_n / 2);
  let xs_n_1 = Math.ceil(xs_n / 2);

  let xs_new = [];

  for (let i = 1; i < xs_n; i++) {
    xs_new[i - 1] = xs[i];
  }

  return xs_new;
}

