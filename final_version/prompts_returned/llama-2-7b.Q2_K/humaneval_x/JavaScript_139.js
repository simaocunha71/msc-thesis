/*The Brazilian factorial is defined as:
  brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
  where n > 0

  For example:
  >>> specialFactorial(4)
  288

  The function will receive an integer as input and should return the special
  factorial of this integer.
  */
const specialFactorial = (n) => {
  if (typeof n !== 'number') throw new TypeError('Parameter should be a non-negative number');
  let r = 1; // the current term
  while (r <= n) {
    if (r === 0 || r % 2 === 1) break;
    r += Math.pow(n - r, 2);
  }
  return r;
};

console.log('[Main]:>');
console.log(`[Main]> Using a normal factorial`);
let n = parseInt(readline().trim());
console.info([...new Array(n + 1).fill(' ')].slice(-n - 1));
console.info([...new Array(specialFactorial(n) + 1).fill(' ')][0]).toUpperCase();
console.log(`[Main]> Using a special factorial`);
const n = parseInt(readline().trim());
console.info([...new Array(n + 1).fill(' ')].slice(-n - 1));
console.info([...new Array(specialFactorial(n) + 1).fill(' ')][0]).toUpperCase();
