const orderByPoints = (nums) => {
  const arr = [];
  for (let i of nums) {
    let sum = 0;
    while (i > 0) {
      sum += i % 10;
      i = Math.floor(i / 10);
    }
    arr.push([sum, i]);
  }
  return arr.sort((a, b) => a[0] - b[0]).map(a => a[1]);
};
