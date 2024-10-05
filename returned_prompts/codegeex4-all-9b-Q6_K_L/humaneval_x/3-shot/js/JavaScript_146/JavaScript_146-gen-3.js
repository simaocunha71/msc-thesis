  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    let num = nums[i];
    if (num > 10 && num % 2 == 1) {
      let first_digit = Math.floor(Math.abs(num) / Math.pow(10, Math.floor(Math.log10(Math.abs(num))))).toString();
      let last_digit = (num % 10).toString();
      if (first_digit % 2 == 1 && last_digit % 2 == 1) {
        count += 1;
      }
    }
  }
  return count;
}