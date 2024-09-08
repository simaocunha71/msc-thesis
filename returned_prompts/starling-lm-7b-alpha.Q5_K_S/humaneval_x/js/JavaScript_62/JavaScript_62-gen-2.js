  let result = [];
  result.push(xs[1]);
  for (let i = 2; i < xs.length; i++) {
    result.push(result[i - 2] + xs[i] * i);
  }

  return result;
}



