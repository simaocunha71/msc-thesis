  if (xs.length % 2 == 1) {
    return undefined;
  }

  if (Math.abs(xs[xs.length - 1]) < 1e-6) {
    return undefined;
  }

  var left = 0;
  var right = xs[xs.length - 2];
  var middle = 0;
  var diff = 1;
  var count = 0;

  while (diff > 1e-6) {
    middle = Math.floor((left + right) / 2);
    diff = middle - right;
    count += 1;
    if (count > 1000) {
      return undefined;
    }
    if (poly(xs, middle) > 0) {
      right = middle;
    } else {
      left = middle;
    }
  }

  return middle;
}



