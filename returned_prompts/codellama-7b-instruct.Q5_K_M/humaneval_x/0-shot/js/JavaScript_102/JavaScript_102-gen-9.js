const chooseNum = (x, y) => {
  let result = -1;
  for (let i = x; i <= y; i++) {
    if (i % 2 === 0) {
      result = i;
      break;
    }
  }
  return result;
};
