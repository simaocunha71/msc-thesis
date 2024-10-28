```javascript
const prodSigns = (arr) => {
  if (!arr.length) return null;

  const productOfSigns = arr.reduce((acc, curr) => acc * (curr >= 0 ? 1 : -1), 1);
  const sumOfMagnitudes = arr.reduce((acc, curr) => acc + Math.abs(curr), 0);

  return productOfSigns * sumOfMagnitudes;
};
```