  if (xs.length % 2 == 1) {
    return null;
  }

  var midpoint = xs.length / 2;

  while (xs[midpoint] == 0) {
    midpoint -= 1;
  }

  var right = xs.slice(midpoint + 1);
  var left = xs.slice(0, midpoint + 1);

  while (right.length > 0 && left.length > 0) {
    if (right[0] == 0) {
      right.shift();
    }
    if (left[0] == 0) {
      left.shift();
    }

    if (right[0] * left[0] < 0) {
      return (right[0] / left[0]) * (midpoint - left.length);
    }

    right.shift();
    left.shift();
  }

  return null;
}



