  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    let firstDigit = Math.floor(nums[i] / 10).toString()[0];
    let lastDigit = nums[i] % 10;
    if (
      firstDigit != '0' &&
      lastDigit != '0' &&
      (
        (
          firstDigit == '1' &&
          lastDigit == '1' ||
          firstDigit == '3' &&
          lastDigit == '3' ||
          firstDigit == '5' &&
          lastDigit == '5' ||
          firstDigit == '7' &&
          lastDigit == '7' ||
          firstDigit == '9' &&
          lastDigit == '9'
        )
      )
    ) {
      count++;
    }
  }

  return count;
}



