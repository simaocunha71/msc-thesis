const chooseNum = (x, y) => {
  let maxEven = -1;
  for (let i = x; i <= y; i++) {
    if (i % 2 === 0) {
      maxEven = i;
    }
  }
  return maxEven;
};