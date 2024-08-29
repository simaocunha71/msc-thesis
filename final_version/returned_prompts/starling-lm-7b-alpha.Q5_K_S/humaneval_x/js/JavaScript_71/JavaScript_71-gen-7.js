  if (a + b > c && a + c > b && b + c > a) {
    const s = (a + b + c) / 2;
    return Math.sqrt(s * (s - a) * (s - b) * (s - c));
  } else {
    return -1;
  }
}



