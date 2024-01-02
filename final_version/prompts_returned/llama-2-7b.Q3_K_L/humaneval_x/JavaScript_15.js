/* Return a string containing space-delimited numbers starting from 0 upto n inclusive.
  >>> stringSequence(0)
  '0'
  >>> stringSequence(5)
  '0 1 2 3 4 5'
  */
const stringSequence = (n) => {
  let res = '';
  for (let i = 0; i < n + 1; ++i) res += ` ${i}`;
  return res;
}

/* Return an array containing all the numbers that are divisible by 3, and a number
  upto n inclusive.
   >>> array(n)(2)
   [0,6]
*/
const array = (n) => {
  let arr = [];
  for (let i = 0; i < n + 1; ++i) if (i % 3 === 0) arr.push(i);
  return arr;
}

/* Return an array containing all the numbers that are divisible by 5, and a number
   upto n inclusive.
    >>> array(n)(4)
   [1,2,4]
*/
const arrayFour = (n) => {
  let arr = [];
  for (let i = 0; i < n + 1; ++i) if (i % 5 === 0) arr.push(i);
  return arr;
}

/* Return an array containing all the numbers that are divisible by both 3 & 4, and a number upto n inclusive.
   >>> arrayFour(n)(6)
   [12]
*/
const arraySix = (n) => {
  let arr = [];
  for (let i = 0; i < n + 1; ++i) if (i % 4 === 0 && i % 3 === 0) arr.push(i);
  return arr;
}

/* Return the number of characters in a string.
   >>> lengthString('abcde')
   'e'
*/
const lengthString = (str) => {
  return str[str.length - 1];
}
