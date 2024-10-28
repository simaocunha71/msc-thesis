  let count = 0;
  for (let num of nums) {
    if (num > 10) {
      if (Math.floor(Math.abs(num) / 10) % 2 !== 0 && num % 10 % 2 !== 0) {
        count++;
      }
    }
  }
  return count;
}