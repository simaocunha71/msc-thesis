  const factors = [];
  for(let i = 2; a !== 1; i++){
    while(a % i === 0){
      factors.push(i);
      a = a / i;
    }
  }
  return factors.filter((item, pos, self) => self.indexOf(item) === pos).length === 3 && factors.every(isPrime);
}

function isPrime(num) {
  for(let i = 2; i < num; i++)
    if(num % i === 0) return false;
  return num !== 1;
}



