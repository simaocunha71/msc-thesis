  var result = [];
  if (n == 0) {
    return result;
  }

  for (var i = 2; i < n; i++) {
    if (isPrime(i)) {
      result.push(i);
    }
  }

  return result;
}



