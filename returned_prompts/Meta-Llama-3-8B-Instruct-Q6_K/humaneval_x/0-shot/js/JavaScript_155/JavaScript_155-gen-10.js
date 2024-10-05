Here is the solution using JavaScript:
```
const evenOddCount = (num) => {
  let evenCount = 0;
  let oddCount = 0;
  const numStr = num.toString();
  for (let i = 0; i < numStr.length; i++) {
    const digit = parseInt(numStr[i]);
    if (digit % 2 === 0) {
      evenCount++;
    } else {
      oddCount++;
    }
  }
  return [evenCount, oddCount];
};
```
Here's an explanation of the code:

1. We initialize two variables `evenCount` and `oddCount` to 0 to keep track of the number of even and odd digits respectively.
2. We convert the input `num` to a string using the `toString()` method.
3. We loop through each character (digit) in the string using a `for` loop.
4. For each digit, we use the `parseInt()` method to convert it to an integer.
5. We check if the digit is even by using the modulo operator (`%`). If the remainder is 0, it's even, otherwise it's odd.
6. We increment the corresponding count variable (`evenCount` or `oddCount`) based on the result.
7. Finally, we return an array containing the `evenCount` and `oddCount` values.

You can test this function with the examples you provided:
```
console.log(evenOddCount(-12)); // [1, 1]
console.log(evenOddCount(123)); // [1, 2]
```
I hope this helps! Let me know if you have any questions. 😊

Update:
If you want to make the code more concise, you can use the `reduce()` method to count the even and odd digits:
```
const evenOddCount = (num) => {
  return [num.toString().split('').reduce((acc, digit) => digit % 2 === 0 ? [...acc, 1] : acc, []), num.toString().split('').reduce((acc, digit) => digit % 2 !== 0 ? [...acc, 1] : acc, [])];
};
```
This code uses the `split()` method to split the string into an array of digits, and then uses the `reduce()` method to count the even and odd digits. The `reduce()` method takes an initial value (`[]` in this case), and for each digit, it