  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  const fibonacci = (num) => {
    let a = 1, b = 1;
    for(let i = 3; i <= num; i++){
      let temp = b;
      b = a + b;
      a = temp;
    }
    return b;
  }

  let count = 0, fib = 1;
  while(count < n){
    fib++;
    if(isPrime(fib)){
      count++;
    }
  }
  return fib;
}



