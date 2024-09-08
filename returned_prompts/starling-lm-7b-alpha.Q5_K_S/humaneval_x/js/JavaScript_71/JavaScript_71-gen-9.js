  if (a + b <= c || b + c <= a || a + c <= b) {
    return -1;
  }
  let s = (a + b + c) / 2;
  return Math.sqrt(s * (s - a) * (s - b) * (s - c));
}



