/*
  This function takes two positive numbers x and y and returns the 
  biggest even integer number that is in the range [x, y] inclusive. If 
  there's no such number, then the function should return -1.

  For example:
  chooseNum(12, 15) = 14
  chooseNum(13, 12) = -1
  */
const chooseNum = (x, y) => {
  if (x % 2 !== 0) {
    x++;
  }
  if (y % 2 !== 0) {
    y--;
  }
  while (x <= y) {
    if (x % 2 === 0) {
      return x;
    }
    x++;
  }
  return -1;
};
