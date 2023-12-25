/*
  Given a positive integer n, return the count of the numbers of n-digit
  positive integers that start or end with 1.
  */
const startsOneEnds = (n) => {
  let i;
  let j;
  let counter;
  // if (n < 10) console.log('n too small...'); return -1;
  for (i = n + 1; i >= 2; i--) {
    if ((i % 4 === 0 && i / 4 > 9) || (i % 4 !== 0)) {
      counter += (i / 10);
    } else break;
  }
  for (j = n - 2; j >= 1; j--) {
    if ((j % 4 === 3 && j / 4 > 9) || (j % 4 !== 0)) {
      counter += (i / 10);
    } else break;
  }
  return counter;
};
