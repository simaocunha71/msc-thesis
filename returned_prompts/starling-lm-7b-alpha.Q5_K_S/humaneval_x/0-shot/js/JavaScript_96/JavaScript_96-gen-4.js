const primes = [];
let num = 2;

while (primes.length < n && num < n) {
  if (isPrime(num)) {
    primes.push(num);
  }
  num++;
}

return primes;

};

function isPrime(num) {
  for (let i = 2; i < num; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return num > 1;
}

console.log(countUpTo(5)); //=> [2,3]
console.log(countUpTo(11)); //=> [2,3,5,7]
console.log(countUpTo(0)); //=> []
console.log(countUpTo(20)); //=> [2,3,5,7,11,13,17,19]
console.log(countUpTo(1)); //=> []
console.log(countUpTo(18)); //=> [2,3,5,7,11,13,17]

*/

In this solution, we first define a function called `countUpTo` which takes a non-negative integer `n` as an argument. We initialize an empty array called `primes` to store the prime numbers. We also initialize a variable `num` with the value 2, as the first prime number is always 2.

Inside the `while` loop, we check if the length of the `primes` array is less than `n` and if `num` is less than `n`. If both conditions are true, we enter the loop.

Inside the loop, we call the `isPrime` function to check if the current value of `num` is a prime number. If it is, we push it to the `primes` array. We then increment the value of `num` by 1.

Once the `while` loop finishes, we return the `primes` array, which contains all the prime numbers less than `n` and less than or equal to `n`.

The `isPrime` function is a helper function that takes a number `num` as an argument and checks if