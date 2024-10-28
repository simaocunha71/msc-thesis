/*This function takes two positive numbers x and y and returns the
  biggest even integer number that is in the range [x, y] inclusive. If 
  there's no such number, then the function should return -1.

  For example:
  chooseNum(12, 15) = 14
  chooseNum(13, 12) = -1
  */
const chooseNum = (x, y) => {
  let start = 0;
  let end = 0;
  let result = 0;

  if (x % 2 !== 0) {
    x++;
  }
  if (y % 2 !== 0) {
    y--;
  }
  start = x;
  end = y;
  for (let i = start; i <= end; i += 2) {
    result = i;
  }
  if (result > 0) {
    return result;
  }
  return -1;
}
