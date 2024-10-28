  let count = 0;
  for (let num of nums) {
    if (num > 10) {
      let first_digit = Math.floor(Math.abs(num) / 10);
      let last_digit = Math.abs(num) % 10;
      if (first_digit % 2 !== 0 && last_digit % 2 !== 0) {
        count++;
      }
    }
  }
  return count;
}