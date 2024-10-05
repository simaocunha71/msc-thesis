  for (let i = 2; i < Math.sqrt(a); i++) {
    if (a % i == 0) {
      return false;
    }
  }

  if (a % 2 == 0 || a % 3 == 0 || a % 5 == 0) {
    return false;
  }

  return true;
}



