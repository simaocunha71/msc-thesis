  let count = 0;
  for (let num of nums) {
    if (Math.abs(num) > 10 && (Math.floor(Math.abs(num) / 10) % 2 !== 0 && num % 10 % 2 !== 0)) {
      count++;
    }
  }
  return count;
}