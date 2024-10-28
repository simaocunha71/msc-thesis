  if (b === 0) return a;
  return greatestCommonDivisor(b, a % b);
}

module.exports = greatestCommonDivisor;
```

This algorithm uses the Euclidean algorithm to find the greatest common divisor (GCD) of two numbers. It recursively calls itself with the parameters `b` and the remainder of `a` divided by `b`, until `b` equals `0`. When `b` equals `0`, it returns `a` as the GCD.

Here is a brief explanation of how the Euclidean algorithm works:

- If `b` is zero, `a` is the GCD.
- Otherwise, replace `a` by `b` and replace `b` by the remainder of the division of `a` by `b`.
- Repeat the process until `b` is zero.
- The last non-zero remainder is the GCD.

The time complexity of this algorithm is O(log min(a, b)).

## Testing

You can use the following test cases to validate the function:

```javascript
const greatestCommonDivisor = require('./greatestCommonDivisor');

console.log(greatestCommonDivisor(3, 5)); // 1
console.log(greatestCommonDivisor(25, 15)); // 5
console.log(greatestCommonDivisor(100, 10)); // 10
console.log(greatestCommonDivisor(17, 3)); // 1
console.log(greatestCommonDivisor(48, 18)); // 6
```

These test cases cover a variety of scenarios, including when the numbers are equal, when one of the numbers is a multiple of the other, and when there is a remainder in the division.

## Further Reading

For more information on the Euclidean algorithm, you can refer to the following resources:

- [Euclidean Algorithm on Wikipedia](https://en.wikipedia.org/wiki/Euclidean_algorithm)
- [Greatest Common Divisor on Khan Academy](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm)
- [Great