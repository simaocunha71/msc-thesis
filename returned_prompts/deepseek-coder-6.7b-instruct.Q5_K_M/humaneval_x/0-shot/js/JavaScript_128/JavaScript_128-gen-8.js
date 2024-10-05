  if (arr.length === 0) return null;

  let signProduct = 1;
  let sum = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < 0) {
      signProduct *= -1;
    } else if (arr[i] > 0) {
      signProduct *= 1;
    } else {
      return 0;
    }

    sum += Math.abs(arr[i]);
  }

  return signProduct * sum;
}

console.log(prodSigns([1, 2, 2, -4])) //== -9
console.log(prodSigns([0, 1])) //== 0
console.log(prodSigns([])) //== null

```


## 8. Count Characters
```javascript
