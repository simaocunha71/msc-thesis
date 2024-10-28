To determine whether the result of multiplying two fractions is a whole number, you need to check whether the numerator of the result is divisible by the denominator. Here is how you can do it:

1. Calculate the numerator of the result by multiplying the numerators of the fractions.
2. Calculate the denominator of the result by multiplying the denominators of the fractions.
3. Check if the numerator of the result is divisible by the denominator.

Here's the step-by-step explanation:

1. Split the input strings by '/' to get the numerator and denominator of the fractions.
2. Multiply the numerators to get the numerator of the result.
3. Multiply the denominators to get the denominator of the result.
4. Check if the numerator of the result is divisible by the denominator. If it is, return true, otherwise, return false.

Here's the code to implement the above steps:

```javascript
function simplify(x, n) {
  const [xNum, xDen] = x.split('/');
  const [nNum, nDen] = n.split('/');

  const resultNum = parseInt(xNum) * parseInt(nNum);
  const resultDen = parseInt(xDen) * parseInt(nDen);

  return resultNum % resultDen === 0;
}
```

This function takes two fractions as input, splits them into numerator and denominator, multiplies the numerators and denominators, and checks if the result is a whole number. It returns true if it is, and false otherwise.

For example, if you call `simplify("1/5", "5/1")`, it will return true because the result of multiplying 1/5 and 5/1 is a whole number. On the other hand, if you call `simplify("1/6", "2/1")`, it will return false because the result of multiplying 1/6 and 2/1 is not a whole number.

Here are some test cases to verify the correctness of the function:

```javascript
console.log(simplify("1/5", "5/1")); // true