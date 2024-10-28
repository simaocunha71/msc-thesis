  let count = 0;
  for (const num of arr) {
    let sum = 0;
    if (num < 0) {
      sum -= num % 10;
      num = -num;
    }
    while (num > 0) {
      sum += num % 10;
      num = Math.floor(num / 10);
    }
    if (sum > 0) {
      count += 1;
    }
  }
  return count;
}