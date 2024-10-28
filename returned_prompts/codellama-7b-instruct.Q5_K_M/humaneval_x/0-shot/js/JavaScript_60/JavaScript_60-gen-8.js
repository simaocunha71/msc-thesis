/*
  This is a solution that works for positive integers.
  It uses a loop that runs from 1 to n, and adds each number to a sum.
  I'm not sure how this solution will work for negative or float numbers.
  */

const sumToN = (n) => {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
}

