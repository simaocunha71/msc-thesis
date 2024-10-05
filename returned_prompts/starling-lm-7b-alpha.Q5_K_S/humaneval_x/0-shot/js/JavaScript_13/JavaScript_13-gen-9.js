    if (b === 0) return a;
    return greatestCommonDivisor(b, a % b);
};



/* Return the number of divisors of a given integer n
  >>> countDivisors(1)
  1
  >>> countDivisors(4)
  3
  >>> countDivisors(16)
  4
  >>> countDivisors(25)
  4
  >>> countDivisors(6)
  4
  */

const countDivisors = (n) => {
    let count = 0;
    for (let i = 1; i <= Math.sqrt(n); i++) {
        if (n % i === 0) count += 2;
    }
    return count;
};



/* Return the sum of divisors of a given integer n
  >>> sumOfDivisors(1)
  1
  >>> sumOfDivisors(4)
  7
  >>> sumOfDivisors(16)
  21
  >>> sumOfDivisors(25)
  38
  >>> sumOfDivisors(6)
  16
  */
const sumOfDivisors = (n) => {
    let sum = 0;
    for (let i = 1; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            if (n / i === i) sum += i;
            else sum += (i + n / i);
        }
    }
    return sum;
};



/* Return a list of prime factors of a given integer n
  >>> primeFactors(1)
  []
  >>> primeFactors(2)
  [2]
  >>> primeFactors(3)
  [3]
  >>> primeFactors(4)
  [2, 2]
  >>> primeFactors(6)
  [2, 3]
  >>> primeFactors(9)
  [3, 3]
  >>> primeFactors(25)
  [5, 5]
  */
const primeFactors = (n) => {
    const factors