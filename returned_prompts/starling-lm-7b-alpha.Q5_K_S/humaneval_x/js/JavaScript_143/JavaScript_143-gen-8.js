  const isPrime = (n) => {
    for (let i = 2; i < n; i++) {
      if (n % i == 0) {
        return false;
      }
    }
    return true;
  };

  const words = sentence.split(" ");
  let result = "";
  for (const word of words) {
    if (isPrime(word.length)) {
      result += word + " ";
    }
  }
  return result;
}



