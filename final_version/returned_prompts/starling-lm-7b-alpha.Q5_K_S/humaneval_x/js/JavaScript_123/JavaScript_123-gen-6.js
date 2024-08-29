  const collatz = (num) => {
    let result = [];
    while (num != 1) {
      if (num % 2 == 0) {
        result.push(num / 2);
        num = num / 2;
      } else {
        result.push(num * 3 + 1);
        num = num * 3 + 1;
      }
    }
    result.push(1);
    return result;
  };

  const getOdd = (nums) => {
    let result = [];
    for (let i = 0; i < nums.length; i++) {
      if (nums[i] % 2 != 0) {
        result.push(nums[i]);
      }
    }
    return result;
  };

  return getOdd(collatz(n));
}



