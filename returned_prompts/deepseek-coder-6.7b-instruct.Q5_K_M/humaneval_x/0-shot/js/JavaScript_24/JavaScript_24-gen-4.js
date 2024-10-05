  for(let i = Math.floor(n/2); i >= 1; i--){
    if(n % i === 0){
      return i;
    }
  }
}

console.log(largestDivisor(15));

// Output: 5
```

## 2. Binary Search

```js
