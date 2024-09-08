  let count = 0;

  for (let i = 0; i < nums.length; i++) {
    let number = Math.abs(nums[i]);
    if (number > 10 && (number % 10 % 2 == 1) && (number / 10 % 10 % 2 == 1)) {
      count += 1;
    }
  }

  return count;
}



