  let s = (a + b + c) / 2;
  if (a + b > c && a + c > b && b + c > a) {
    return Math.sqrt(s * (s - a) * (s - b) * (s - c)).toFixed(2);
  } else {
    return -1;
  }
}



