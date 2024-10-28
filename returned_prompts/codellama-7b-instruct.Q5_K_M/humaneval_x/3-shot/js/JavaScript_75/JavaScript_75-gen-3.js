  for (let i = 2; i < a; i++) {
    if (a % i == 0) {
      let b = a / i;
      for (let j = 2; j < b; j++) {
        if (b % j == 0) {
          return false;
        }
      }
      return true;
    }
  }
  return false;
}



