  if (arr.length == 0) {
    return null;
  }
  let signProduct = 1;
  let sum = 0;
  for (let num of arr) {
    if (num != 0) {
      signProduct *= Math.sign(num);
      sum += Math.abs(num);
    }
  }
  return signProduct * sum;
}