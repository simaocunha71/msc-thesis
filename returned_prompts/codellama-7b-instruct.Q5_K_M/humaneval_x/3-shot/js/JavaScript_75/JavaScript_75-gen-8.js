  for (let i = 2; i < a; i++) {
    if (a % i == 0) {
      var count = 0;
      while (a % i == 0) {
        a /= i;
        count++;
      }
      if (count > 2) {
        return false;
      }
    }
  }
  return true;
}



