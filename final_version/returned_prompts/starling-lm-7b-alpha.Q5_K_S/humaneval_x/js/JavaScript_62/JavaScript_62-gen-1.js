  if (xs.length == 0) {
    return [];
  } else {
    return [xs[1], ...xs.map((x, i) => i * x)];
  }
}



