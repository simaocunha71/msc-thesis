/*Given an integer. return a list that has the number of even and odd digits respectively.

   Example:
      evenOddCount(-12) ==> [1, 1]
      evenOddCount(123) ==> [1, 2]
  */
const evenOddCount = (num) => {
  let strNum = num + '';
  const strs = []
  for (let i = 0; i < strNum.length; i++) {
    let digitStr = strNum[i];
    if (!isNaN(digitStr)) {
      strs.push(strNum[i] % 2 ? '1' : '0');
    } else if (isNaN(digitStr)) {
      strs.push('-');
    }
  }
  return strs;
};