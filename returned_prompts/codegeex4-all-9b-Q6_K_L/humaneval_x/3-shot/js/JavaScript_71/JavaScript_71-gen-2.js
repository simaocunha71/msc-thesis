  if (a + b <= c || a + c <= b || b + c <= a) {
    return -1;
  }
  let s = (a + b + c) / 2;
  let area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
  return Math.round(area * 100) / 100;
}



