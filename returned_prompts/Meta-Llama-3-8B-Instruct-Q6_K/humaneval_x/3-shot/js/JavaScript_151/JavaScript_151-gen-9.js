  let sum = 0;
  for (let num of lst) {
    if (num > 0 && typeof num === 'number' && num % 1 === 0) {
      sum += Math.pow(num, 2);
    }
  }
  return sum;
}?



