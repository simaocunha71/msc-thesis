  if ((a + b > c) && (a + c > b) && (b + c > a)) {
    let s = (a + b + c) / 2.0;
    return Number((Math.sqrt(s * (s - a) * (s - b) * (s - c))).toFixed(2));
  } else {
    return -1;
  }
}



