/*
  Given two positive integers a and b, return the even digits between a
  and b, in ascending order.

  For example:
  generateIntegers(2, 8) => [2, 4, 6, 8]
  generateIntegers(8, 2) => [2, 4, 6, 8]
  generateIntegers(10, 14) => []
  */
const generateIntegers = (a, b) => {
  const map = new Map();
  let sum = a + b; // the length of the list
  if (sum < 5) return [];
  while (map.has(sum)) {
    sum += 2;
  }
  for (let i = 0; i <= sum / 2; i++) {
    let currentSum = a + b - i;
    const evenDigits = Number(currentSum).toString().split('').filter((char) => char % 2 === 0);
    map.set(i, ...evenDigits);
  }
  return Array.from(map.keys());
};
