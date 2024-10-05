  const isPrime = (number) => {
    for(let i = 2, sqrt = Math.sqrt(number); i <= sqrt; i++)
      if(number % i === 0) return false; 
    return number > 1;
  }

  return isPrime(string.length);
}



