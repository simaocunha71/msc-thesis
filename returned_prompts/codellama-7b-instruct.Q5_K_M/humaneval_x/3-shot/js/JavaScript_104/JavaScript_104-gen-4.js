  var result = [];

  for (let i = 0; i < x.length; i++) {
    if (x[i] % 2 == 1) {
      result.push(x[i]);
    }
  }

  return result.sort((a, b) => a - b);
}



