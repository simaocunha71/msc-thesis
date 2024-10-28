  if (xs.length % 2 != 0) {
    throw new Error('xs must have even length');
  }
  var max_coeff = Math.abs(xs[xs.length - 1]);
  var x = 0.0;
  if (max_coeff > 0) {
    x = -xs[xs.length - 1] / max_coeff;
  }
  var roots = [x];
  for (var i = xs.length - 3; i >= 0; i -= 2) {
    var p = poly(xs.slice(0, i + 2), x);
    var q = poly(xs.slice(i + 2), x);
    var new_x = x - p / q;
    roots.push(new_x);
    x = new_x;
  }
  return roots;
}

/*
  Given a list of coefficients, find all roots of polynomial.
  >>> round(roots([1, 2, 3])[0], 2) # f(x) = 1 + 2x + 3x^2
  -1.5
  >>> round(roots([-6, 11, -6, 1])[0], 2) # (x - 1)