  if (n < 4) {
    return false;
  }
  if (n % 2 === 0) {
    return false;
  }
  if (n % 4 === 0) {
    return true;
  }
  return isEqualToSumEven(n - 2);
}



