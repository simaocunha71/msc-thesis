  // your code here
  return xs.slice(0, xs.length - 1).concat(xs.slice(1, xs.length - 1).map((e, i) => e * (i + 1)));
}
