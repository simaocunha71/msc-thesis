
    let result = 1;
    let oddDigit = false;
    while (n > 0) {
        const digit = n % 10;
        if (digit % 2 !== 0) {
            result *= digit;
            oddDigit = true;
        }
        n = Math.floor(n / 10);
    }

    return oddDigit ? result : 0;
};

console.log(digits(235)); // 15




/*Given a positive integer n, return the product of the odd digits.
  Return 0 if all digits are even.
  For example:
  digits(1)  == 1
  digits(4)  == 0
  digits(235) == 15
  */

function digits(n) {
    let result = 1;
    let oddDigit = false;
    while (n > 0) {
        const digit = n % 10;
        if (digit % 2 !== 0) {
            result *= digit;
            oddDigit = true;
        }
        n = Math.floor(n / 10);
    }
    return oddDigit ? result : 0;
}

console.log(digits(235)); // 15




/*Given a positive integer n, return the product of the odd digits.
  Return 0 if all digits are even.
  For example:
  digits(1)  == 1
  digits(4)  == 0
  digits(235) == 15
  */

function digits(n) {
    let result = 1;
    let oddDigit = false;
    while (n > 0) {
        const digit = n % 10;
        if (digit % 2 !== 0) {
            result *= digit;
            oddDigit = true;
        }
        n = Math.floor(n / 10);
    }
    return oddDigit ? result : 0;
}

console.log