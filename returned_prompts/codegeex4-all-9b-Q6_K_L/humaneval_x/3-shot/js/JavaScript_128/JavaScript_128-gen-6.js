  if (arr.length == 0) {
    return null;
  } else {
    let product = 1;
    let sum = 0;
    for (const i of arr) {
      if (i < 0) {
        product *= -1;
      }
      sum += Math.abs(i);
    }
    return product * sum;
  }
}