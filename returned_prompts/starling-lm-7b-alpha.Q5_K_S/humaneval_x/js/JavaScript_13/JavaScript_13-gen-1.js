  while (b != 0) {
    let r = a % b;
    a = b;
    b = r;
  }
  return a;
}



