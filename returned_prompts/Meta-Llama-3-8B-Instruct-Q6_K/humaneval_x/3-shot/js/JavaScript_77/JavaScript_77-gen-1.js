  for (let i = 1; Math.pow(i, 3) <= a; i++) {
    if (Math.pow(i, 3) === a) {
      return true;
    }
  }
  return false;
}