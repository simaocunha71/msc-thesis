  if (a < 100) {
    for (let i = 2; i < a; i++) {
      if (a % i == 0) {
        for (let j = 2; j < i; j++) {
          if (i % j == 0) {
            return false;
          }
        }
      }
    }
    return true;
  }
}



