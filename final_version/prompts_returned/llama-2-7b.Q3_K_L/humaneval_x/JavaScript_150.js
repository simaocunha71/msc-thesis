/*A simple program which should return the value of x if n is 
  a prime number and should return the value of y otherwise.

  Examples:
  for xOrY(7, 34, 12) == 34
  for xOrY(15, 8, 5) == 5
  
  */
const xOrY = (n, x, y) => {
  if (!x || !y) return;
  const p = factorial(n);
  let ret = 0;
  for (let i of [...Array(p.length)]) {
    const a = n % Math.pow(2, i);
    //console.log('a:' + a);
    if (!a || !x && a == 1 || y && a == 0) ret += 1;
    else break;
  }
  return ret;
}
const factorial = (n) => {
  const arr = [];
  for (let i of [...Array(n + 1)]) arr.push(i);
  return arr;
};
console.log('xOrY(7, 34, 12): ', xOrY(7, 34, 12));
//console.log('xOrY(15, 8, 5)', xOrY(15, 8, 5));
