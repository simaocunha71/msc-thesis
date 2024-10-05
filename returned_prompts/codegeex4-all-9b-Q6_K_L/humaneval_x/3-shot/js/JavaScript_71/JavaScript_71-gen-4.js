  if (a + b <= c || a + c <= b || b + c <= a) {
    return -1;
  }

  var s = (a + b + c) / 2;
  var area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
  return Math.round(area * 100) / 100;
}



