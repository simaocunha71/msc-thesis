  let p = (a + b + c) / 2;
  let s = Math.sqrt(p * (p - a) * (p - b) * (p - c));
  if (a + b > c && a + c > b && b + c > a && a != 0 && b != 0 && c != 0) {
    return Math.round(s * 100) / 100;
  } else {
    return -1;
  }
}



