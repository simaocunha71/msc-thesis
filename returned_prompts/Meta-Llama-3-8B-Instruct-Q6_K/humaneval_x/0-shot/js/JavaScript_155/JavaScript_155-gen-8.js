Here is a possible solution:
```
const evenOddCount = (num) => {
  let evenCount = 0;
  let oddCount = 0;

  while (num !== 0) {
    const digit = num % 10;
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
Here's an explanation of the code:

1. We initialize two counters, `evenCount` and `oddCount`, to keep track of the number of even and odd digits respectively.
2. We loop until the input number `num` becomes 0.
3. In each iteration, we extract the last digit of the number using the modulo operator (`num % 10`).
4. We check if the digit is even by using the modulo operator again (`digit % 2 === 0`). If it is, we increment `evenCount`. Otherwise, we increment `oddCount`.
5. We update the number by removing the last digit using the floor division operator (`Math.floor(num / 10)`).
6. Finally, we return an array containing the counts of even and odd digits.

You can test this function with the examples you provided:
```
console.log(evenOddCount(-12)); // [1, 1]
console.log(evenOddCount(123)); // [1, 2]
```
I hope this helps! Let me know if you have any questions. 😊 