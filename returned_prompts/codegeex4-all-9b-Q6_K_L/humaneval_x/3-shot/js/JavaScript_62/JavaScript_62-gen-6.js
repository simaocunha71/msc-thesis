  var result = [];
  for (let i = 0; i < xs.length - 1; i++) {
    result.push(xs[i + 1] * (i + 1));
  }
  return result;
}