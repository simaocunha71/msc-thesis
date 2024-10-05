  var d = n;

  while (d > 1) {
    if (n % d == 0) {
      return d;
    }
    d -= 1;
  }

  return 1;
}



