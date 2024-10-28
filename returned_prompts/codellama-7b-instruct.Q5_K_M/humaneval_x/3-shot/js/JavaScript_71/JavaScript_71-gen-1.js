  if (a + b > c && b + c > a && a + c > b) {
    var s = (a + b + c) / 2;
    var area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
    return Math.round(area * 100) / 100;
  }
  return -1;
}



