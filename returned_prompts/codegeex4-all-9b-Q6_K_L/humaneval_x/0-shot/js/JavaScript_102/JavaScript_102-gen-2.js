const chooseNum = (x, y) => {
  if (x > y) {
    return -1;
  }
  for (let i = Math.max(x, y); i >= Math.min(x, y); i--) {
    if (i % 2 === 0) {
      return i;
    }
  }
  return -1;
};

console.log(chooseNum(12, 15)); // 14
console.log(chooseNum(13, 12)); // -1
console.log(chooseNum(14, 15)); // 14
console.log(chooseNum(15, 15)); // 14
console.log(chooseNum(15, 14)); // 14
console.log(chooseNum(16, 15)); // 16