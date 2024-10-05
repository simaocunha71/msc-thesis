Here is the solution to the problem:
```
const countUpTo = (n) => {
  if (n <= 1) return [];

  const result = [];
  let i = 2;

  while (i < n) {
    if (isPrime(i)) {
      result.push(i);
    }
    i++;
  }

  return result;
};

const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) return false;
  }
  return true;
};
```
Explanation:

The `countUpTo` function takes an integer `n` as input and returns an array of the first `n` integers that are prime numbers and less than `n`.

The function uses a while loop to iterate from `2` to `n-1`. For each integer `i` in this range, it checks if `i` is a prime number using the `isPrime` function. If `i` is prime, it is added to the result array.

The `isPrime` function takes an integer `num` as input and returns a boolean indicating whether `num` is a prime number. It does this by checking if `num` has any divisors other than `1` and itself. If `num` has any divisors, it is not prime, and the function returns `false`. Otherwise, it returns `true`.

The `countUpTo` function returns the result array once the while loop has finished iterating.

Example usage:
```
console.log(countUpTo(5)); // [2, 3]
console.log(countUpTo(11)); // [2, 3, 5, 7]
console.log(countUpTo(0)); // []
console.log(countUpTo(20)); // [2, 3, 5, 7, 11, 13, 17, 19]
console.log(countUpTo(1)); // []
console.log(countUpTo(18)); // [2, 3, 5, 7, 11, 13, 17]
``` 