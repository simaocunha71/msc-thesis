  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    let num = nums[i];
    if (num > 10 && (num % 10) % 2 === 1 && Math.floor(num / 10) % 10 === 1) {
      count += 1;
    }
  }
  return count;
}



