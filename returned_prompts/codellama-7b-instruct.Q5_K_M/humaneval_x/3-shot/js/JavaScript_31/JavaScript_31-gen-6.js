  if (n < 2) {
    return false;
  } else if (n == 2) {
    return true;
  } else {
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i == 0) {
        return false;
      }
    }
    return true;
  }
}



