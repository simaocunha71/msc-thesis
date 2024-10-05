Here is a JavaScript solution for the problem:

```javascript
const simplify = (x, n) => {
  const [xNum, xDen] = x.split('/').map(Number);
  const [nNum, nDen] = n.split('/').map(Number);
  
  const gcd = (a, b) => {
    if (b === 0) return a;
    return gcd(b, a % b);
  };
  
  const newXDen = gcd(xDen, nDen);
  const newXNum = xNum * (nDen / newXDen);
  const newNDen = xDen / newXDen;
  const newNNum = nNum * (xDen / newNDen);
  
  return newXNum === parseInt(newXNum) && newNNum === parseInt(newNNum);
};
```

This function first splits the input strings into numerator and denominator, then calculates the greatest common divisor (GCD) of the two denominators. It then calculates the new numerators and denominators by dividing the original numerators and denominators by the GCD. Finally, it checks if the new numerators are integers by comparing them with their integer part. If they are the same, it returns true; otherwise, it returns false.