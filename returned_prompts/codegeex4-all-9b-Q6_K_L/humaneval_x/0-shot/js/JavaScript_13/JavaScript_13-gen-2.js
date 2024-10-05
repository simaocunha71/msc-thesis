The greatest common divisor (GCD) of two integers a and b is the largest number that divides both of them without leaving a remainder.

Here is a function that calculates the GCD of two integers using the Euclidean algorithm:

```javascript
const greatestCommonDivisor = (a, b) => {
  while (b !== 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}
```

This function uses a while loop to repeatedly calculate the remainder of a divided by b, until b is equal to 0. The GCD is then the last value of a.

Let's test the function with the provided examples:

```javascript
console.log(greatestCommonDivisor(3, 5)); // 1
console.log(greatestCommonDivisor(25, 15)); // 5
```

Both examples return the correct result.