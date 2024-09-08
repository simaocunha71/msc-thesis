  let i = 0;
  while (true) {
    if (x == 1) {
      return true;
    }
    if (i >= 60) {
      return false;
    }
    if (x % n === 0) {
      x /= n;
      i += 1;
    } else {
      return false;
    }
  }
}



