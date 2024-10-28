  var largestPrime;
  var sumOfDigits = 0;

  for (let i = lst.length - 1; i >= 0; i--) {
    if (isPrime(lst[i])) {
      largestPrime = lst[i];
      break;
    }
  }

  while (largestPrime > 0) {
    sumOfDigits += largestPrime % 10;
    largestPrime = Math.floor(largestPrime / 10);
  }

  return sumOfDigits;
}

function isPrime(num) {
  for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
    if(num % i === 0) return false; 
  return num > 1;
}



