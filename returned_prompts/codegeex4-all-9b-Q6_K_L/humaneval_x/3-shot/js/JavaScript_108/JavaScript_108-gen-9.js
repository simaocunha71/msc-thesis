  let count = 0;
  for (const i of arr) {
    let sum = 0;
    let num = Math.abs(i);
    while (num != 0) {
      sum += num % 10;
      num = Math.floor(num / 10);
    }
    if (sum > 0) {
      count += 1;
    }
  }
  return count;
}