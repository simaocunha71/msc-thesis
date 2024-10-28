  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false;
    return num > 1;
  }

  let words = sentence.split(' '),
      result = [];

  for(let word of words) {
    if(isPrime(word.length)) result.push(word);
  }

  return result.join(' ');
}



