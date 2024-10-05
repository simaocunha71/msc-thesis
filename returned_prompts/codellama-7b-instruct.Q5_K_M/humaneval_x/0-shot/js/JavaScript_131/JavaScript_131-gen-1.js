  const nums = n.toString().split('');
  const oddNums = [];
  let result = 1;

  for (let i = 0; i < nums.length; i++) {
    if (parseInt(nums[i]) % 2 !== 0) {
      oddNums.push(nums[i]);
    }
  }

  for (let i = 0; i < oddNums.length; i++) {
    result *= parseInt(oddNums[i]);
  }
  return result;
}

