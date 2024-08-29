  let result = [0];

  for (let i = 0; i < xs.length; i++) {
    if (i != 0) {
      result[i] = result[i - 1] + (i + 1) * xs[i];
    }
  }

  return result;
}



