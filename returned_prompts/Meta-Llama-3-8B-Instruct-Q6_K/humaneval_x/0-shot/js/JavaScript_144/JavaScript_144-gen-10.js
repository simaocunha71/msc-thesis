Here is a JavaScript solution for the problem. It first parses the input strings into fractions, then multiplies them and checks if the result is a whole number.

```javascript
const simplify = (x, n) => {
    const [a, b] = x.split('/').map(Number);
    const [c, d] = n.split('/').map(Number);
    
    const numerator = a * c;
    const denominator = b * d;
    
    return gcd(denominator, numerator) === numerator;
};

const gcd = (a, b) => {
    while (b !== 0) {
        const temp = b;
        b = a % b;
        a = temp;
    }
    return a;
};
```

This solution works by first parsing the input strings into fractions, then multiplying them together. It uses the gcd (Greatest Common Divisor) function to simplify the fraction. The gcd function is a helper function that calculates the gcd of two numbers using the Euclidean algorithm. The simplify function then checks if the result is a whole number by comparing it to its denominator. If they are equal, the result is a whole number and the function returns true; otherwise, it returns false.