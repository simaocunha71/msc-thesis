  let c = 0;
  while (Math.pow(c, 3) <= a) {
    if (Math.pow(c, 3) === a) {
      return true;
    }
    c++;
  }
  return false;
}