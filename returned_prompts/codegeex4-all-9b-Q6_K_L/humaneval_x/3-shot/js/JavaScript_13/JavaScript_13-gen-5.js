  while (b > 0) {
    let tmp = a;
    a = b;
    b = tmp % b;
  }
  return a;
}



