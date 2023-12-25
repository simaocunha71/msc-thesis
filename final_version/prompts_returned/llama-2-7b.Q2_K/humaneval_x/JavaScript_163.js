/*
  Given two positive integers a and b, return the even digits between a
  and b, in ascending order.

  For example:
  generateIntegers(2, 8) => [2, 4, 6, 8]
  generateIntegers(8, 2) => [2, 4, 6, 8]
  generateIntegers(10, 14) => []
  */
const generateIntegers = (a, b) => {
  const ints = [];
  for (let i = a; i < b + 1; i++) {
    if (!ints.includes(i)) {
      ints.push(i);
    }
  }

  return ints;
};
