  if (arr.length === 0) return null;
  let product = 1;
  let sum = 0;
  for (const num of arr) {
    product *= Math.sign(num);
    sum += Math.abs(num);
  }
  return product * sum;
}