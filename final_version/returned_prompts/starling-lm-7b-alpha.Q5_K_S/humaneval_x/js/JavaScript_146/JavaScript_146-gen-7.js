  let count = 0;
  for(let i = 0; i < nums.length; i++) {
    let strNum = nums[i].toString();
    if (nums[i] > 10 && strNum[0] % 2 !== 0 && strNum[strNum.length - 1] % 2 !== 0) {
      count += 1;
    }
  }
  return count;
}



