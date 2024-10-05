const specialFilter = (nums) => {

  let count = 0;

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    if (num > 10 && (num % 10 > 1 && num % 10 < 9) && (num % 100 > 10 && num % 100 < 90)) {
      count++;
    }
  }

  return count;
};

