  for(let i = n-1; i > 0; i--){
    if(n % i === 0){
      return i;
    }
  }
};

console.log(largestDivisor(15));

// Output: 5

```



## 10. Write a JavaScript function to find the first n Fibonacci sequence numbers.

```javascript
