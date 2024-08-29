  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    let num = nums[i];
    let firstDigit = Math.floor(num / 10);
    let lastDigit = num % 10;
    if (num > 10 && firstDigit % 2 != 0 && lastDigit % 2 != 0) {
      count++;
    }
  }
  return count;
}



