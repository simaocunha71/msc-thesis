  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    let str = nums[i].toString();
    if (str[0] % 2 !== 0 && str[str.length - 1] % 2 !== 0 && nums[i] > 10) {
      count += 1;
    }
  }
  return count;
}



