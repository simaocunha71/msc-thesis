To solve this problem, we can follow these steps:

1. Parse the input strings into numerator and denominator fractions.
2. Calculate the product of the fractions.
3. Simplify the product fraction to the lowest terms.
4. Check if the numerator of the simplified product fraction is equal to 1.
5. Return true if the condition in step 4 is met, otherwise return false.

Here's a detailed explanation of the steps with code examples:

Step 1: Parse the input strings into numerator and denominator fractions.
To convert the string representation of a fraction into a number, we can use the `split()` method to split the string at the '/' character. Then, we can convert the numerator and denominator parts into numbers using the `parseInt()` function.

Here's an example of how to parse the fractions from the input strings:

```javascript
const xParts = x.split('/');
const xNumerator = parseInt(xParts[0]);
const xDenominator = parseInt(xParts[1]);

const nParts = n.split('/');
const nNumerator = parseInt(nParts[0]);
const nDenominator = parseInt(nParts[1]);
```

Step 2: Calculate the product of the fractions.
To calculate the product of the fractions, we can multiply the numerators and the denominators separately. Then, we can multiply the results to get the product of the fractions.

Here's an example of how to calculate the product of the fractions:

```javascript
const productNumerator = xNumerator * nNumerator;
const productDenominator = xDenominator * nDenominator;
```

Step 3: Simplify the product fraction to the lowest terms.
To simplify the product fraction to the lowest terms, we can use the Euclidean algorithm to find the greatest common divisor (GCD) of the product numerator and the product denominator. Then, we can divide both the product numerator and the product denominator by the GCD to get the simplified product fraction.

Here's an example of how to simplify the product fraction to the lowest terms:

```javascript