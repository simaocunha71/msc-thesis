  let count = 0;
  for (const num of nums) {
    if (num > 10 && num % 2 == 1) {
      const str = num.toString();
      const first_digit = parseInt(str[0]);
      const last_digit = parseInt(str[str.length - 1]);
      if (first_digit % 2 == 1 && last_digit % 2 == 1) {
        count += 1;
      }
    }
  }
  return count;
}