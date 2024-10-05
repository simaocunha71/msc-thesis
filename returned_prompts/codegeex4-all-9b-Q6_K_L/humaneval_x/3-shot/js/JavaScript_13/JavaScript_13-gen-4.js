  while (b != 0) {
    var t = b;
    b = a % b;
    a = t;
  }
  return a;
}



