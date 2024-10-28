  let sum = 0;
  
  for (let i = 0; i < k; i++) {
    let len = arr[i].toString().length;
    if (len <= 2) {
      sum += arr[i];
    }
  }
  
  return sum;
};

console.log(addElements([111,21,3,4000,5,6,7,8,9], 4));
// Output: 24
```

### JavaScript Solution

```javascript
