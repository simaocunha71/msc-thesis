  if (xs.length % 2 != 0) {
    throw new Error('Only polynomials with even number of coefficients are supported');
  }

  if (xs.filter(x => x != 0).length < 2) {
    throw new Error('Polynomial must have at least 2 non zero coefficients');
  }

  var min_x = -1.0 * (Math.abs(xs[1]) / (2.0 * xs[0]));
  var max_x = -1.0 * min_x;

  while (true) {
    var mid_x = (min_x + max_x) / 2.0;

    if (poly(xs, mid_x) == 0.0) {
      return mid_x;
    }

    if (poly(xs, min_x) * poly(xs, mid_x) <= 0.0) {
      max_x = mid_x;
    } else {
      min_x = mid_x;
    }
  }
}



