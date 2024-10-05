  let count = 0;
  for (let num of nums) {
    if (num > 10) {
      let str = num.toString();
      let first_digit = parseInt(str[0]);
      let last_digit = parseInt(str[str.length - 1]);
      if (first_digit % 2 !== 0 && last_digit % 2 !== 0) {
        count++;
      }
    }
  }
  return count;
}