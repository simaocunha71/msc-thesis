  if ((a + b) <= c || (a + c) <= b || (b + c) <= a) {
    return -1;
  }

  let s = (a + b + c) / 2;
  return Math.sqrt(s * (s - a) * (s - b) * (s - c));
}



