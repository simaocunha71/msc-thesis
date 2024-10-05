To solve this problem, you need to follow these steps:

1. Parse the x and n strings to get the numerator and denominator values. You can use the split method to separate the numerator and denominator, and then convert them to integers using the parseInt method. For example, for x = "1/5", the numerator would be 1 and the denominator would be 5.

2. Calculate the least common denominator (LCD) of the two fractions using the formula LCD = (numerator1 * denominator2) / (gcd(numerator1, denominator2)) and the gcd(a, b) function to find the greatest common divisor of two numbers. You can use the modulus operator (%) to find the remainder when one number is divided by another. For example, for numerator1 = 1 and denominator1 = 5, the gcd(1, 5) is 1. For numerator1 = 7 and denominator1 = 10, the gcd(7, 10) is 1.

3. Calculate the new numerator and denominator values by multiplying the original numerator and denominator by the LCD. For example, for x = "1/5", the new numerator would be (1 * LCD) and the new denominator would be (5 * LCD). For x = "7/10", the new numerator would be (7 * LCD) and the new denominator would be (10 * LCD).

4. Check if the new numerator is a whole number by using the modulus operator (%) to find the remainder when the new numerator is divided by the new denominator. If the remainder is zero, then the expression evaluates to a whole number and you can return true. Otherwise, the expression does not evaluate to a whole number and you can return false.

Here is an example implementation of the simplify function in JavaScript:

```javascript
function gcd(a, b) {
  while (b !== 0) {
    let r = a % b;
    a = b;
    b = r;
  }
  return a;
}

function simplify(x, n) {
  let [numeratorX, denominatorX] = x.split