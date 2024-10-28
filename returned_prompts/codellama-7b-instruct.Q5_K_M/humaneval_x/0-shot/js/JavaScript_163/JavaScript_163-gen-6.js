/*
  Given two positive integers a and b, return the even digits between a
  and b, in ascending order.

  For example:
  generateIntegers(2, 8) => [2, 4, 6, 8]
  generateIntegers(8, 2) => [2, 4, 6, 8]
  generateIntegers(10, 14) => []
  */
const generateIntegers = (a, b) => {
  const arr = []
  for (let i = a; i <= b; i++) {
    if (i % 2 === 0) arr.push(i)
  }
  return arr
}

