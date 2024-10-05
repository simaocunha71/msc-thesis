  for (let i = 2; i < a; i++) {
    if (a % i == 0) {
      let j = a / i;
      for (let k = 2; k < j; k++) {
        if (j % k == 0) {
          return false;
        }
      }
      return true;
    }
  }
  return false;
}



