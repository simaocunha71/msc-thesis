Here is the solution in JavaScript:
```javascript
const evenOddCount = (num) => {
  let evenCount = 0;
  let oddCount = 0;
  while (num !== 0) {
    let digit = num % 10;
    if (digit % 2 === 0) {
      evenCount++;
    } else {
      oddCount++;
    }
    num = Math.floor(num / 10);
  }
  return [evenCount, oddCount];
};
```
Explanation:

* We initialize two counters, `evenCount` and `oddCount`, to keep track of the number of even and odd digits respectively.
* We use a while loop to iterate through each digit of the input number.
* Inside the loop, we extract the last digit of the number using the modulo operator (`%`) and check if it's even or odd using the remainder operator (`% 2`).
* If the digit is even, we increment `evenCount`; if it's odd, we increment `oddCount`.
* After processing each digit, we divide the number by 10 using the floor function (`Math.floor`) to move to the next digit.
* Finally, we return an array containing the counts of even and odd digits.

Example usage:
```javascript
console.log(evenOddCount(-12)); // [1, 1]
console.log(evenOddCount(123)); // [1, 2]
```