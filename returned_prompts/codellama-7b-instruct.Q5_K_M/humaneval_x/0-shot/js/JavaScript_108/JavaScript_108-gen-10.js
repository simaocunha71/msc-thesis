const countNums = (arr) => {
  const nums = arr.reduce((acc, num) => {
    if (num > 0) {
      acc.push(num);
    }
    return acc;
  }, []);
  return nums.length;
};
