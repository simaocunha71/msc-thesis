  let result = [];

  for(let i = 1; i <= n; i++){
    if(i%2 === 0){
      let fact = 1;
      for(let j = 1; j <= i; j++){
        fact *= j;
      }
      result.push(fact);
    }else{
      let sum = 0;
      for(let j = 1; j <= i; j++){
        sum += j;
      }
      result.push(sum);
    }
  }

  return result;
}

console.log(f(5));


// This solution uses two nested loops and checks every index for even or odd value.
// If it's even, then calculate its factorial and add it to the result array.
// If it's odd, then calculate the sum of numbers from 1 to that index and add it to the result array.
// Finally, return the result array.
// This solution is efficient as it has a time complexity of O(n^2).



```

## Question 2

```javascript
