  while(b) {
    var t = b;
    b = a % b;
    a = t;
  }
  return a;
}



