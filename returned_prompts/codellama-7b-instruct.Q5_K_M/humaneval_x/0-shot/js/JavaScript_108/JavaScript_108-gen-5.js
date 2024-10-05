const countNums = (arr) => {
  const result = arr.reduce((acc, num) => {
    if (num > 0) {
      acc++;
    }
    return acc;
  }, 0);
  return result;
};
