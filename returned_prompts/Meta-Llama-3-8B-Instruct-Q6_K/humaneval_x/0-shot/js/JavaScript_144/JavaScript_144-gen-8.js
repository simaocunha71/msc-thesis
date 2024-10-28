```javascript
const simplify = (x, n) => {
    const [xN, xD] = x.split('/');
    const [nN, nD] = n.split('/');

    const gcd = (a, b) => {
        if (b === 0) return a;
        return gcd(b, a % b);
    };

    const newXN = xN * nD;
    const newXD = xD * nN;

    const g = gcd(newXN, newXD);
    return newXN / g === newXD / g;
};
```


This function uses the concept of greatest common divisor (GCD) to simplify the fractions. The GCD is used to reduce the numerator and denominator to their simplest form. The function splits the input strings into their numerator and denominator, calculates the GCD of the new numerator and denominator, and then checks if the simplified fractions are equal. If they are equal, the function returns true, otherwise it returns false.