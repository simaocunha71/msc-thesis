const countNums = (arr) => {
  const nums = arr.map((n) => {
    if (n < 0) return -n;
    return n;
  });
  return nums.reduce((acc, cur) => {
    if (cur > 0) return acc + 1;
    return acc;
  }, 0);
};

