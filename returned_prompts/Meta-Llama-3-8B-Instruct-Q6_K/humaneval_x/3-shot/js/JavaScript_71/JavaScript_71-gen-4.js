  if (a + b > c && a + c > b && b + c > a) {
    var s = (a + b + c) / 2;
    var area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
    return Math.round(area * 100) / 100;
  } else {
    return -1;
  }
}
