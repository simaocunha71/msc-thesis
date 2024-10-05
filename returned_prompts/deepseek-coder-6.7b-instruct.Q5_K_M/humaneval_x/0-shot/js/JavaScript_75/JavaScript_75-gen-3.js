  let factors = [];
  for(let i = 2; i <= a; i++){
    while(a % i === 0){
      factors.push(i);
      a = a / i;
    }
  }
  return factors.every(el => {
    let count = 0;
    for(let i = 2; i <= el/2; i++){
      if(el % i === 0){
        count++;
      }
    }
    return count === 0;
  }) && factors.length === 3;
}

console.log(isMultiplyPrime(30)); // should return true
console.log(isMultiplyPrime(100)); // should return false
console.log(isMultiplyPrime(300)); // should return true
console.log(isMultiplyPrime(1000)); // should return false

Explanation: 
This function works by first finding all the prime factors of the input number. 
Then it checks if all these factors are prime. If they are, and there are exactly 3 factors, it returns true. Otherwise, it returns false.

*/

/*
