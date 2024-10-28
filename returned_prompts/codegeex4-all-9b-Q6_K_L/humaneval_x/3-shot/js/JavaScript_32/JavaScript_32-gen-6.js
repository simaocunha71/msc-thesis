  return findZeroHelper(xs, xs.length - 1, 0, 10);
}

const findZeroHelper = (xs, n, x, count) => {
  if (count == 0) {
    return x;
  }
  var x1 = x - (poly(xs, x) / poly(xs, x + 0.01));
  if (Math.abs(x1 - x) < 0.00001) {
    return findZeroHelper(xs, n - 2, x1, count - 1);
  }
  return findZeroHelper(xs, n, x1, count);
}

const round = (n, p) => {
  return Math.round(n * Math.pow(10, p)) / Math.pow(10, p);
}



