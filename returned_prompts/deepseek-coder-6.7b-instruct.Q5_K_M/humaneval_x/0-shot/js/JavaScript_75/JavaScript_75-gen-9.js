  let factors = [];
  let count = 0;

  for(let i = 2; i <= a; i++){
    while(a % i == 0){
      if(factors.indexOf(i) == -1){
        factors.push(i);
      }
      a = a / i;
      count++;
    }
  }

  if(count == 3 && factors.every(isPrime)){
    return true;
  }else{
    return false;
  }

  function isPrime(num){
    for(let j = 2, sqrt = Math.sqrt(num); j <= sqrt; j++)
      if(num % j === 0) return false; 
    return num > 1;
  }
}

console.log(isMultiplyPrime(30));  //== true
console.log(isMultiplyPrime(21));  //== false
console.log(isMultiplyPrime(42));  //== true
console.log(isMultiplyPrime(100)); //== false

*/

// ----------------------
/*
// The function isMultiplyPrime(a) returns true if the given number (a) is the multiplication of 3 prime numbers.
// It does this by using a for loop to find the prime factors of the number. 
// If the number of factors is 3 and all the factors are prime numbers, the function will return true. Otherwise, it will return false.
*/
// ----------------------

// ----------------------
/*
// The function isPrime(num) returns true if the given number (num) is a prime number. 
// It does this by checking if the number has any factors other than 1 and itself. 
// If the number has any factors, the function will return false. Otherwise, it will return true.
*/
// ----------------------
// ----------------------

// ----------------------
/*
// The function isMultiplyPrime(a) returns true if the given number (a) is the multiplication of 3 prime numbers.
// It does this by using a for loop to find the prime factors of the number. 
// If the number of factors