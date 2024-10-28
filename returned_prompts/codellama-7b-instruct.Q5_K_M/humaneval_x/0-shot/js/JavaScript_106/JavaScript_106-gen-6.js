/* 
  [1, 2, 6, 24, 15]
  1! = 1
  2! = 2
  3! = 6
  4! = 24
  5! = 120
*/

const f = (n) => {
  let result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      result.push(i * (i - 1) * (i - 2) * (i - 3) * (i - 4));
    } else {
      result.push(i + (i - 1) + (i - 2) + (i - 3) + (i - 4));
    }
  }
  return result;
};