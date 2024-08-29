  if (xs.length == 0) {
    return [];
  } else {
    return [xs[1] * xs[0], ...derivative(xs.slice(2))];
  }
}



