  var factors = [];
  var divisor = 2;

  while(n > 1){
    while(n % divisor === 0){
      factors.push(divisor);
      n = n / divisor;
    }
    divisor++;
  }

  return factors;
}



