  if(arr.length === 0)
    return null;

  let sum = 0;
  let productSign = 1;

  for(let i = 0; i < arr.length; i++) {
    if(arr[i] < 0) {
      productSign *= -1;
      sum += Math.abs(arr[i]);
    } else if(arr[i] > 0) {
      sum += arr[i];
    }
  }

  return productSign * sum;
};

module.exports = {prodSigns};

```

## 4. Fibonacci Series
```
