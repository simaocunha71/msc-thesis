  let result = true;
  while (x >= 1) {
    x = x / n;
    if (x % 1 != 0) {
      result = false;
      break;
    }
  }
  return result;
}



