  var primes = ['2', '3', '5', '7', 'B', 'D'];
  return num.split('').filter(c => primes.includes(c)).length;
}