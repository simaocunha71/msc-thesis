  let result = [];
  for (let i = 0; i < xs.length; i++) {
    if (i == 0) {
      result.push(xs[i + 1] * (i + 1));
    } else {
      result.push(xs[i + 1] * i);
    }
  }
  return result;
}



