  if (a + b > c && b + c > a && a + c > b) {
    const s = (a + b + c) / 2.0;
    return Math.round(Math.sqrt(s * (s - a) * (s - b) * (s - c)) * 100) / 100;
  }
  return -1;
}



