  let result = 1;

  for (let i = 1; i <= n; i++) {
    result *= i;
  }

  return result;
};

console.log(specialFactorial(4)); // 288









*/

/*
In this simple Kata you will create a function that takes a number n and returns the sum of all the multiples of 3 and 5 under n (excluding n).

For example:

sumMultiples(10) == 23
# because the multiples of 3 under 10 are 3, 6, and 9; the multiples of 5 are 5 and 10

sumMultiples(20) == 78
# because the multiples of 3 under 20 are 3, 6, 9, and 12; the multiples of 5 are 5, 10, and 15

Note: the multiples of 3 are all the odd numbers, while the multiples of 5 are all the numbers that are divisible by 5.

You can assume that the input is a positive number greater than or equal to 1.

*/


function sumMultiples(n) {
  let sum = 0;
  for (let i = 1; i < n; i++) {
    if (i % 3 === 0 || i % 5 === 0) {
      sum += i;
    }
  }
  return sum;
}

console.log(sumMultiples(10)); // 23






































































































































