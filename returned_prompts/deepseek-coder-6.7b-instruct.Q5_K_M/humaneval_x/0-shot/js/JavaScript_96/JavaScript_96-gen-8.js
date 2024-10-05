let arr = [];
  for(let i = 2; i < n; i++){
    if(isPrime(i)){
      arr.push(i);
    }
  }
  return arr;
}

const isPrime = (num) => {
  for(let i = 2; i < num; i++){
    if(num % i === 0) return false;
  }
  return num > 1;
}

console.log(countUpTo(5)); //[2, 3]
console.log(countUpTo(11)); //[2, 3, 5, 7]
console.log(countUpTo(0)); // []
console.log(countUpTo(20)); //[2, 3, 5, 7, 11, 13, 17, 19]
console.log(countUpTo(1)); // []
console.log(countUpTo(18)); //[2, 3, 5, 7, 11, 13, 17]

//Time complexity O(n^2)
//Space complexity O(n)

//Optimizing with the Sieve of Eratosthenes algorithm

const countUpToOptimized = (n) => {
  let primes = [];
  let sieve = Array(n).fill(true);

  for (let i = 2; i < n; i++) {
    if (sieve[i]) {
      primes.push(i);
      for (let j = i * 2; j < n; j += i) {
        sieve[j] = false;
      }
    }
  }
  return primes;
}

console.log(countUpToOptimized(5)); //[2, 3]
console.log(countUpToOptimized(11)); //[2, 3, 5, 7]
console.log(countUpToOptimized(0)); // []
console.log(countUpToOptimized(20)); //[2, 3, 5, 7, 11, 13, 