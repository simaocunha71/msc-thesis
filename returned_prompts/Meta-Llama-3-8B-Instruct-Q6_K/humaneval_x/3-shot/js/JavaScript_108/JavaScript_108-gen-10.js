  let count = 0;
  for (const num of arr) {
    if (num < 0) {
      num = -num;
    }
    let sum = 0;
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