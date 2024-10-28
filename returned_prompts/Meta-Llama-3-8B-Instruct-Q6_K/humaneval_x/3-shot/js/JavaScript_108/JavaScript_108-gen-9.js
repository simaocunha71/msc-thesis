  let count = 0;
  for (let num of arr) {
    let sum = 0;
    let isNegative = num < 0;
    if (isNegative) {
      num = -num;
    }
    while (num > 0) {
      sum += num % 10;
      num = Math.floor(num / 10);
    }
    if (sum > 0) {
      count++;
    }
  }
  return count;
}