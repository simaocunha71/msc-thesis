  for(let i = n - 1; i > 0; i--) {
    if(n % i === 0) {
      return i;
    }
  }
}

console.log(largestDivisor(15)); // 5

/*
  Explaination:
  The function 'largestDivisor' takes an integer as an argument and returns the largest number that divides 'n' evenly, smaller than 'n'. 
  It does this by looping from 'n - 1' down to '1' (inclusive), and checking if 'n' is divisible by the current number (i) using the modulo operator. 
  If it is, the function returns that number. 
  This will be the largest number that evenly divides 'n', as it checks every number in decreasing order.
*/

```

## Q3:

```javascript
