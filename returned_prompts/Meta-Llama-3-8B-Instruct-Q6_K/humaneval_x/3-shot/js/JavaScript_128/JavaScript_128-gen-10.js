  if (arr.length == 0) {
    return null;
  }

  let product = 1;
  let sum = 0;

  for (let num of arr) {
    if (num == 0) {
      return 0;
    }
    product *= Math.sign(num);
    sum += Math.abs(num);
  }

  return product * sum;
}