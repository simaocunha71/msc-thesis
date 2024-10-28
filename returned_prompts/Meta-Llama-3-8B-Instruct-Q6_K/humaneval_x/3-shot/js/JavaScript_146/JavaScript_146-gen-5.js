  let count = 0;
  for (let num of nums) {
    if (num > 10) {
      let first_digit = Math.floor(Math.abs(num) / 10);
      let last_digit = Math.floor(Math.abs(num) % 10);
      if (first_digit % 2 !== 0 && last_digit % 2 !== 0) {
        count++;
      }
    }
  }
  return count;
}
// You can also use regex for this problem.
// const specialFilter = (nums) => {
//   return nums.filter(num => num > 10 && String(num).match(/^1|3|5|7|9$/)).length;
// }