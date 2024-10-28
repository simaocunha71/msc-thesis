  var primes = [2, 3, 5, 7];
  var result = 0;
  for (var i = 0; i < num.length; i++) {
    var digit = parseInt(num[i], 16);
    if (primes.includes(digit)) {
      result += 1;
    }
  }
  return result;
}