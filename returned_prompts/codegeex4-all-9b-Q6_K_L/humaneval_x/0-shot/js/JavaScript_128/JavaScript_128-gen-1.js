/*
  You are given an array arr of integers and you need to return
  sum of magnitudes of integers multiplied by product of all signs
  of each number in the array, represented by 1, -1 or 0.
  Note: return null for empty arr.

  Example:
  >>> prodSigns([1, 2, 2, -4]) == -9
  >>> prodSigns([0, 1]) == 0
  >>> prodSigns([]) == null
  */
const prodSigns = (arr) => {
  if (arr.length === 0) return null;
  let signProduct = 1;
  let sum = 0;
  arr.forEach((num) => {
    if (num === 0) return;
    signProduct *= num > 0 ? 1 : -1;
    sum += Math.abs(num);
  });
  return sum * signProduct;
};