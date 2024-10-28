The unit digit of a number is the rightmost digit. For example, the unit digit of 148 is 8.

To solve this problem, we can use the modulo operator (`%`) to get the unit digit of each number, multiply them together, and return the result.

Here is the solution:
```javascript
const multiply = (a, b) => {
  return (a % 10) * (b % 10);
}
```
Here's how it works:
```javascript
multiply(148, 412) // returns 16
// a % 10 = 8, b % 10 = 2, 8 * 2 = 16

multiply(19, 28) // returns 72
// a % 10 = 9, b % 10 = 8, 9 * 8 = 72

multiply(2020, 1851) // returns 0
// a % 10 = 0, b % 10 = 1, 0 * 1 = 0

multiply(14, -15) // returns 20
// a % 10 = 4, b % 10 = -5, 4 * (-5) = -20
```
Note that the modulo operator (`%`) returns the remainder of the division of the number by the divisor. In this case, we use it to get the unit digit of each number by dividing by 10. The unit digit is the remainder of the division. For example, 148 divided by 10 is 14 with a remainder of 8, so the unit digit of 148 is 8. Similarly, 412 divided by 10 is 41 with a remainder of 2, so the unit digit of 412 is 2. etc.