
function countUpTo(n) {
  let primes = [];
  for (let i = 2; i < n; i++) {
    let isPrime = true;
    for (let j = 2; j < i; j++) {
      if (i % j === 0) {
        isPrime = false;
      }
    }
    if (isPrime) {
      primes.push(i);
    }
  }
  return primes;
}

console.log(countUpTo(5)); // [2,3]
console.log(countUpTo(11)); // [2,3,5,7]
console.log(countUpTo(0)); // []
console.log(countUpTo(20)); // [2,3,5,7,11,13,17,19]
console.log(countUpTo(1)); // []
console.log(countUpTo(18)); // [2,3,5,7,11,13,17]

/*
  The function works as follows:
  1. Initialize an empty array called primes.
  2. For each integer i from 2 to n - 1, inclusive, do the following:
    a. Set isPrime to true.
    b. For each integer j from 2 to i - 1, inclusive, do the following:
      i. If i is divisible by j, set isPrime to false.
    c. If isPrime is true, push i to the primes array.
 3. Return the primes array.
 */

};


































































































































