  let count = 0;
  for(let i = 0; i < nums.length; i++) {
    let num = Math.abs(nums[i]);
    if(num > 10 && (num % 10 % 2 === 1) && (num / 10000 % 10 % 2 === 1)) {
      count += 1;
    }
  }
  return count;
}



