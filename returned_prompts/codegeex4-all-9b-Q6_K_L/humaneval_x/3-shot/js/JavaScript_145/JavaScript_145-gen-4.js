  return nums.sort((a, b) => sumOfDigits(a) - sumOfDigits(b));
}

const sumOfDigits = (num) => {
  if (num < 0) {
    return -sumOfDigits(-num);
  }
  if (num < 10) {
    return num;
  }
  return num % 10 + sumOfDigits(Math.floor(num / 10));
}



