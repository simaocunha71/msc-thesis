const countNums = (arr) => {
  let count = 0;
  arr.forEach(n => {
    if (n > 0) count++;
  });
  return count;
};
