const chooseNum = (x, y) => {
  if (x > y) {
    return -1;
  }

  let biggestEven = -1;

  for (let i = x; i <= y; i++) {
    if (i % 2 === 0) {
      biggestEven = i;
    }
  }

  return biggestEven;
};

console.log(chooseNum(12, 15)); // 14
console.log(chooseNum(13, 12)); // -1