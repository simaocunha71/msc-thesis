  let count = 0;
  for (const num of arr) {
    let sum = 0;
    while (num != 0) {
      const digit = num % 10;
      sum += digit;
      num = Math.floor(num / 10);
    }
    if (sum > 0) {
      count += 1;
    }
  }
  return count;
}



