  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }
  
  const words = sentence.split(' ');
  let result = '';
  
  for(let i = 0; i < words.length; i++) {
    if(isPrime(words[i].length)) {
      if(result !== '') result += ' ';
      result += words[i];
    }
  }
  
  return result;
}



