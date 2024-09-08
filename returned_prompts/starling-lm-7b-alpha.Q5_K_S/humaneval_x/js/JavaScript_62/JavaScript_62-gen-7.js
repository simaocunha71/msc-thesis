  let result = [];
  if (xs.length == 1) {
    return [0];
  }

  result.push(xs[1]);
  for (let i = 2; i < xs.length; i++) {
    result.push(result[i - 2] + i * xs[i]);
  }

  return result;
}



