  var primeNumbers = [];
  for (var i = 2; i < n; i++) {
    var isPrime = true;
    for (var j = 2; j < Math.sqrt(i); j++) {
      if (i % j == 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      primeNumbers.push(i);
    }
  }
  return primeNumbers;
}



