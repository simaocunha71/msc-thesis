  let factors = [];
  for(let i = 2; i <= a; i++){
    while(a % i === 0){
      factors.push(i);
      a = a / i;
    }
  }
  return factors.length === 3 && factors.every(isPrime);
}

const isPrime = (num) => {
  for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
    if(num % i === 0) return false; 
  return num > 1;
}



