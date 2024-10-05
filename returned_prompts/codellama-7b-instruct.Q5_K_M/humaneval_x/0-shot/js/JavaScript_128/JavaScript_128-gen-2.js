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
  if (!arr.length) return null;

  const product = arr.reduce((acc, curr) => (acc *= Math.sign(curr)), 1);
  const sum = arr.reduce((acc, curr) => (acc += Math.abs(curr)), 0);

  return sum * product;
};

