To solve this problem, we can follow these steps:

1. First, we need to check if n is greater than m. If it is, we return -1, as the problem states that we should return -1 in this case.
2. If n is not greater than m, we can calculate the average of the integers from n to m by adding them together and dividing by 2 (since there are m - n + 1 integers in the range).
3. We round the average to the nearest integer using Math.round().
4. To convert the rounded average to binary, we use the toString(2) method on the result of Math.round(). This converts the number to a binary string representation.
5. Finally, we return the binary representation of the rounded average.

Here's an example implementation of the roundedAvg function:

```javascript
function roundedAvg(n, m) {
  if (n > m) {
    return -1;
  }

  const average = Math.round((n + m) / 2);
  return average.toString(2);
}
```

You can use this function to find the rounded average of the integers from n to m and convert it to binary.

For example, if you call `roundedAvg(10, 20)`, it will return "1111" as the binary representation of the average of the integers from 10 to 20 (which is 15).

Note that if n is greater than m, the function will return -1, as stated in the problem.

I hope this helps! Let me know if you have any more questions.

*/

```javascript
function roundedAvg(n, m) {
  if (n > m) {
    return -1;
  }

  const average = Math.round((n + m) / 2);
  return average.toString(2);
}
```

```javascript
console.log(roundedAvg(1, 5)); // "0b11"
console.log(roundedAvg(7, 5)); // -1
console.log(roundedAvg(10, 20)); // "0b11