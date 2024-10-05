  var result = [];
  var i = 2;

  while (i < n) {
    if (isPrime(i)) {
      result.push(i);
    }
    i += 1;
  }

  return result;
}



