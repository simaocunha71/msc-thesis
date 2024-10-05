```
const prodSigns = (arr) => {
  if (!arr.length) return null;

  let productOfSigns = 1;
  let sumOfMagnitudes = 0;

  for (let num of arr) {
    if (num === 0) {
      return sumOfMagnitudes;
    }
    productOfSigns *= Math.sign(num);
    sumOfMagnitudes += Math.abs(num);
  }

  return productOfSigns * sumOfMagnitudes;
};
```  