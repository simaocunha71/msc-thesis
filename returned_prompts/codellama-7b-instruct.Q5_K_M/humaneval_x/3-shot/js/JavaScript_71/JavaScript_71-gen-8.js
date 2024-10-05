  if (a + b > c && b + c > a && a + c > b) {
    const s = (a + b + c) / 2.0;
    const area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
    return area.toFixed(2);
  } else {
    return -1;
  }
}



