  for (let i = 2; i <= 10; i++) {
    if (a % i == 0) {
      let n = a / i;
      if (n % 2 == 0 && n % 3 == 0) return true;
      if (n % 3 == 0) return true;
      if (n % 2 == 0) return true;
    }
  }

  return false;
}



