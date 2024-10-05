  let start = -10;
  let end = 10;
  let mid;

  while (true) {
    mid = (start + end) / 2;
    if (Math.abs(poly(xs, mid)) < 0.00000001) {
      return mid;
    } else if (poly(xs, mid) > 0) {
      end = mid;
    } else {
      start = mid;
    }
  }
}


