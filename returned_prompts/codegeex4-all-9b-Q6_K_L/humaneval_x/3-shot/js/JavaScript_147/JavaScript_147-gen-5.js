  let count = 0;
  let nums = [];

  for (let i = 1; i <= n; i++) {
    nums.push(i * i - i + 1);
  }

  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        if ((nums[i] + nums[j] + nums[k]) % 3 == 0) {
          count++;
        }
      }
    }
  }

  return count;
}



