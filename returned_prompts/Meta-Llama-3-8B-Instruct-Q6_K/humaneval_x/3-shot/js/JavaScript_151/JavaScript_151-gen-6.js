  let sum = 0;
  for (const num of lst) {
    if (num >= 0 && parseInt(num) === num) {
      if (num % 2 !== 0) {
        sum += Math.pow(num, 2);
      }
    }
  }
  return sum;
}