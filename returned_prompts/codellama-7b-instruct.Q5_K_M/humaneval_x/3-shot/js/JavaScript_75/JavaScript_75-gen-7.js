  for (let i = 2; i < Math.sqrt(a); i++) {
    if (a % i == 0) {
      return false;
    }
  }
  return true;
}



