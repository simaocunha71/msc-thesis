  if (a + b > c && b + c > a && c + a > b) {
    const s = (a + b + c) / 2;
    const area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
    return Math.round(area * 100) / 100;
  } else {
    return -1;
  }
}



