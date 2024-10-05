  let result = [];
  for(let i=1; i<=n; i++) {
    if(i%2 === 0) {
      let fact = 1;
      for(let j=1; j<=i; j++) {
        fact *= j;
      }
      result.push(fact);
    } else {
      let sum = 0;
      for(let j=1; j<=i; j++) {
        sum += j;
      }
      result.push(sum);
    }
  }
  return result;
};

console.log(f(5));

/*
Explanation:
Here, we are creating a function called f which takes one parameter n. We declare an empty array result. 
For each i from 1 to n, we check if i is even or not using the modulus operator. If i is even, we calculate the factorial of i and push it into the result array. 
If i is not even, we calculate the sum of numbers from 1 to i and push it into the result array. Finally, we return the result array.
*/
```

## 4. Factorial and Sum of Odd Indexed Elements

```js
