  if (a + b <= c || a + c <= b || b + c <= a) {
    return -1;
  }

  let p = (a + b + c) / 2.0;
  let area = Math.sqrt(p * (p - a) * (p - b) * (p - c));
  return Math.round(area * 100.0) / 100.0;
}



