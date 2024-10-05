  const isPrime = num => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  const primeFactors = num => {
    let factors = [], i = 2;
    while(i <= num){
      if(num % i === 0 && isPrime(i)){
        factors.push(i);
        num = num / i;
      }
      else{
        i++;
      }
    }
    return factors;
  }

  let factors = primeFactors(a);
  return factors.length === 3 && factors.reduce((a,b) => a*b) === a;
}

console.log(isMultiplyPrime(30)); // true
console.log(isMultiplyPrime(15)); // false
console.log(isMultiplyPrime(30030)); // true
console.log(isMultiplyPrime(12)); // true
console.log(isMultiplyPrime(11)); // false
console.log(isMultiplyPrime(27)); // false
console.log(isMultiplyPrime(646)); // true
console.log(isMultiplyPrime(137)); // false
```





















































































































































































