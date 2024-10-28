const primeLength = (string) => {
  var isPrime = false;
  for (var i = 2; i < string.length; i++) {
    if (string.length % i === 0) {
      isPrime = false;
      break;
    } else {
      isPrime = true;
    }
  }
  return isPrime;
};

