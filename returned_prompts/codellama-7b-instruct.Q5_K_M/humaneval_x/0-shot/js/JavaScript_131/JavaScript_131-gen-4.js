/*
 1. convert the number to a string
 2. use filter to check if the number is odd
 3. use reduce to multiply the odd numbers together
*/
const digits = (n) => {
  let str = String(n);
  return str.split('').filter(num => num % 2 !== 0).reduce((product, num) => product * num, 1);
}
