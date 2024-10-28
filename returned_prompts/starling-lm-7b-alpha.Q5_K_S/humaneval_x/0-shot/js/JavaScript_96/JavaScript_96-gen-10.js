const primes = [2,3];
let i = 5;
while (primes.length < n) {
  let isPrime = true;
  for (let j = 0; j < primes.length; j++) {
    if (i % primes[j] === 0) {
      isPrime = false;
      break;
    }
  }
  if (isPrime) {
    primes.push(i);
  }
  i++;
}
return primes;
};

