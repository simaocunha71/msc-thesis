
const specialFilter = (nums) => {
  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 10) {
      let firstDigit = nums[i].toString()[0];
      let lastDigit = nums[i].toString()[nums[i].toString().length - 1];
      if (firstDigit % 2 != 0 && lastDigit % 2 != 0) {
        count++;
      }
    }
  }
  return count;
};

