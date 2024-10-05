  let sum = 0;
  for (let num of lst) {
    if (num > 0 && num % 1 === 0 && num % 2 !== 0) {
      sum += Math.pow(num, 2);
    }
  }
  return sum;
}