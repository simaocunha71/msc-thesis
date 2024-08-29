  if (x % 2 == 1 && y % 2 == 1) {
    return -1;
  } else {
    if (x % 2 == 1) {
      return x;
    } else {
      if (y % 2 == 1) {
        return y;
      } else {
        return y - 1;
      }
    }
  }
}



