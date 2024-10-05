  const isPrime = num => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  const sumOfDigits = num => {
    return num.toString().split('').reduce((a, b) => {
      return parseInt(a) + parseInt(b);
    }, 0);
  }

  let maxPrime = -1;
  for(let i = 0; i < lst.length; i++){
    if(isPrime(lst[i]) && lst[i] > maxPrime) maxPrime = lst[i];
  }
  return maxPrime != -1 ? sumOfDigits(maxPrime) : null;
}


A: Here are the answers to your questions:

