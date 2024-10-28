  if (x % 2 == 1) {
    x += 1;
  }

  while (x <= y) {
    if (x % 2 == 0) {
      return x;
    }
    x += 1;
  }

  return -1;
}



