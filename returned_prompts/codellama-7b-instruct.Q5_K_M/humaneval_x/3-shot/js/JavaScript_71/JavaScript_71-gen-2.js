  if (a + b > c && b + c > a && c + a > b) {
    var s = (a + b + c) / 2;
    return Math.round((Math.sqrt(s * (s - a) * (s - b) * (s - c)) * 100) / 100);
  } else {
    return -1;
  }
}



