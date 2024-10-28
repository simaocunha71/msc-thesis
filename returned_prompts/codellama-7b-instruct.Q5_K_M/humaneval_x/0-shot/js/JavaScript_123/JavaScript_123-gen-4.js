/*
  The Collatz sequence is a sequence of numbers that starts from any positive integer n. 
  Each term is obtained from the previous term as follows: if the previous term is even, 
  the next term is one half of the previous term. If the previous term is odd, the next 
  term is 3 times the previous term plus 1. 
  The conjecture is that no matter what value of n, the sequence will always reach 1.

  So, we start with the number n, and we apply the Collatz sequence rules on it, and we keep 
  doing that until we reach 1. And at each step, we store the number we get in the array, 
  so that we can return it sorted in increasing order.
*/
const getOddCollatz = (n) => {
  const result = [];
  while (n !== 1) {
    if (n % 2 === 0) {
      n /= 2;
    } else {
      n = 3 * n + 1;
    }
    result.push(n);
  }
  return result;
}

