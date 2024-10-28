  if (a + b > c && b + c > a && c + a > b) {
    const s = (a + b + c) / 2;
    return (Math.sqrt(s * (s - a) * (s - b) * (s - c))).toFixed(2);
  }
  return -1;
};
