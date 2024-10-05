You can use the following approach:

1. Check if n is greater than m. If it is, return -1.
2. Calculate the average of the integers from n to m.
3. Round the average to the nearest integer.
4. Convert the rounded average to binary.
5. Return the binary string prefixed with "0b".

Here is the complete code:

```javascript
const roundedAvg = (n, m) => {
  if (n > m) return -1;

  const avg = Math.round((n + m) / 2);
  const binary = avg.toString(2);

  return "0b" + binary;
}
```

Let's test the function with the provided examples:

```javascript
console.log(roundedAvg(1, 5)); // "0b11"
console.log(roundedAvg(7, 5)); // -1
console.log(roundedAvg(10, 20)); // "0b1111"
console.log(roundedAvg(20, 33)); // "0b11010"
```

The function should return the expected output.