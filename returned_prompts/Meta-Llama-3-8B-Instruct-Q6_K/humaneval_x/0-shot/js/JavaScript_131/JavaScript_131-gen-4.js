Here is a solution for the problem:
```
const digits = (n) => {
  let product = 1;
  let oddDigits = 0;
  while (n > 0) {
    let digit = n % 10;
    if (digit % 2 !== 0) {
      product *= digit;
      oddDigits++;
    }
    n = Math.floor(n / 10);
  }
  return oddDigits > 0 ? product : 0;
};
```
Explanation:
The solution uses a while loop to iterate through each digit of the input number `n`. For each digit, it checks if the digit is odd by using the modulo operator (`%`). If the digit is odd, it multiplies the `product` variable by the digit and increments the `oddDigits` variable. After iterating through all digits, it returns the `product` variable if there were any odd digits, otherwise it returns 0.

Example usage:
```
console.log(digits(1)); // 1
console.log(digits(4)); // 0
console.log(digits(235)); // 15
```