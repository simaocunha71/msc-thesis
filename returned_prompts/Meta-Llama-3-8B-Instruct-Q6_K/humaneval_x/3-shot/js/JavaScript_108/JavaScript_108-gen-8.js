  let count = 0;
  for (let num of arr) {
    let sum = 0;
    if (num < 0) {
      num = -num;
    }
    while (num > 0) {
      sum += Math.floor(num % 10);
      num = Math.floor(num / 10);
    }
    if (sum > 0) {
      count++;
    }
  }
  return count;
} 