const countNums = (arr) => {
  let num = 0;
  for (let i of arr) {
    if (i > 0) {
      num++;
    }
  }
  return num;
};
