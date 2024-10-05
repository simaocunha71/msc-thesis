  let factor = 2;
  let remaining = n;

  while (remaining != 1) {
    if (remaining % factor == 0) {
      remaining /= factor;
    } else {
      factor++;
    }
  }

  return factor;
}



