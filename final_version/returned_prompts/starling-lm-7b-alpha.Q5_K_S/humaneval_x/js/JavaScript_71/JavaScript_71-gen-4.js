  if (a + b > c && a + c > b && b + c > a) {
    let s = (a + b + c) / 2;
    let area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
    return area.toFixed(2);
  } else {
    return -1;
  }
}



