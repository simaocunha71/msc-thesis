  let primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
  let i = 0;
  while(i<primes.length && primes[i]*primes[i]<=a){
    i++;
  }
  let j = 0;
  while(j<primes.length && primes[j]*primes[j]<=a){
    j++;
  }
  let k = 0;
  while(k<primes.length && primes[k]*primes[k]<=a){
    k++;
  }
  if(i<primes.length && j<primes.length && k<primes.length &&
     primes[i]*primes[j]*primes[k] == a) {
    return true;
  } else {
    return false;
  }
}



