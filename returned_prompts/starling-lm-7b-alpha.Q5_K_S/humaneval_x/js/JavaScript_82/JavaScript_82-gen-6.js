  var strLength = string.length;
  var strLengthSqrt = Math.sqrt(strLength);
  var isPrime = true;

  for (let i = 2; i <= strLengthSqrt; i++) {
    if (strLength % i === 0) {
      isPrime = false;
      break;
    }
  }

  return isPrime;
}



