  let result = [];
  for (let i = 1; i < xs.length; i++) {
    result.push(xs[i] * i);
  }
  result.unshift(xs[0]);
  return result;
}



