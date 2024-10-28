  var mid = xs[xs.length - 1];
  var left = 0;
  var right = mid;
  var diff = 1;

  while (diff > 1e-5) {
    mid = (left + right) / 2.0;
    diff = Math.abs(poly(xs, mid));
    if (poly(xs, mid) > 0) {
      right = mid;
    } else {
      left = mid;
    }
  }

  return mid;
}


