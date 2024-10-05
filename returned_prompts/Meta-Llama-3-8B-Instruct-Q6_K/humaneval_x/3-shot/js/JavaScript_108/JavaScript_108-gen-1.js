  let count = 0;
  for (let num of arr) {
    let sum = 0;
    let isNegative = false;
    if (num < 0) {
      num = -num;
      isNegative = true;
    }
    while (num > 0) {
      sum += num % 10;
      num = Math.floor(num / 10);
    }
    if (sum > 0 || (isNegative && sum > 1)) {
      count++;
    }
  }
  return count;
}



