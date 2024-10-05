  if (x > y) {
    if (x % 2 == 0) {
      return x;
    } else {
      return -1;
    }
  } else {
    for (let i = x; i <= y; i++) {
      if (i % 2 == 0) {
        return i;
      }
    }
    return -1;
  }
} 