  let count = 0;
  for (const num of nums) {
    if (num > 10) {
      let str_num = num.toString();
      let first_digit = parseInt(str_num[0]);
      let last_digit = parseInt(str_num[str_num.length - 1]);
      if (first_digit % 2 == 1 && last_digit % 2 == 1) {
        count += 1;
      }
    }
  }
  return count;
}