  const sumOfDigits = (n) => {
    let result = 0;
    while (n > 0) {
      result += n % 10;
      n = Math.floor(n / 10);
    }
    return result;
  }

  const count = (n) => {
    if (n == 0) {
      return 0;
    } else {
      return Math.sign(n) * (Math.abs(n) % 1 == 0 ? 1 : count(Math.floor(Math.abs(n) / 10)));
    }
  }

  return arr.reduce((acc, curr) => acc + count(sumOfDigits(curr)), 0);
}



