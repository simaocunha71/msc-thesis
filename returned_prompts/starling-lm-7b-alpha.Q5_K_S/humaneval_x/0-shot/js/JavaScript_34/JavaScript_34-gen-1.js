  return [...new Set(l)].sort((a, b) => a - b);
};







/*
Return the sum of all elements in the list
  >>> sum(l)
  28
  */
const sum = (l) => {
  return l.reduce((acc, val) => acc + val, 0);
};







/*
Return the product of all elements in the list
  >>> product(l)
  5040
  */
const product = (l) => {
  return l.reduce((acc, val) => acc * val, 1);
};







/*
Return a list with all elements greater than 3
  >>> greaterThan3(l)
  [5, 9, 123]
  */
const greaterThan3 = (l) => {
  return l.filter(num => num > 3);
};







/*
Return a list with all elements divisible by 3
  >>> divisibleBy3(l)
  [3, 9, 123]
  */
const divisibleBy3 = (l) => {
  return l.filter(num => num % 3 === 0);
};







/*
Return a list of the first n elements of the input list
  >>> firstN(l, 3)
  [0, 2, 3]
  */
const firstN = (l, n) => {
  return l.slice(0, n);
};







/*
Return a list of the last n elements of the input list
  >>> lastN(l, 3)
  [3, 5, 9]
  */
const lastN = (l, n) => {
  return l.slice(-n);
};







/*
Return a list with all elements of the input list reversed
  >>> reverse(l)
  [123, 9, 5, 3, 2, 0]
  */
const reverse = (l) => {
  return l.slice().