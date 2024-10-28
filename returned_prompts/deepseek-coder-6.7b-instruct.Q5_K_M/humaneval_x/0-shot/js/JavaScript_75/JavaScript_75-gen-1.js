  let factors = [];
  for(let i = 2; i <= a; i++){
    while(a % i === 0){
      factors.push(i);
      a /= i;
    }
  }
  return factors.every(val => {
    for(let j = 2; j < val; j++){
      if(val % j === 0)
        return false;
    }
    return true;
  }) && factors.length === 3;
}

console.log(isMultiplyPrime(30)); // true
console.log(isMultiplyPrime(100)); // false
console.log(isMultiplyPrime(30030)); // true
console.log(isMultiplyPrime(1000)); // false

// isMultiplyPrime(30)  ->  true (2*3*5 = 30)
// isMultiplyPrime(100) ->  false (2*2*5*5 = 100)
// isMultiplyPrime(30030) -> true (2*3*5*7*11 = 30030)
// isMultiplyPrime(1000) -> false (2*2*2*5*5*5 = 1000)
```

###### Explanation:
The function `isMultiplyPrime` takes in an integer `a` and finds all its factors. If all the factors are prime numbers and the count of factors is equal to 3, then it returns `true`, otherwise `false`.

```javascript
let factors = [];
for(let i = 2; i <= a; i++){
  while(a % i === 0){
    factors.push(i);
    a /= i;
  }
}
```
This loop finds all the factors of `a` by dividing `a` by `i` as long as `a` is divisible by `i`.

```javascript
return factors.every(val => {
  for(let j = 2; j < val; j++){
    if(val % j === 0)
      return