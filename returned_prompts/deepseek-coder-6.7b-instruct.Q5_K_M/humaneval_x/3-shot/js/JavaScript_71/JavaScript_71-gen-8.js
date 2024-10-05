  if (a + b > c && a + c > b && b + c > a) {
    let s = (a + b + c) / 2;
    return Math.round((s - a) * (s - b) * (s - c) * 100) / 100;
  } else {
    return -1;
  }
}



