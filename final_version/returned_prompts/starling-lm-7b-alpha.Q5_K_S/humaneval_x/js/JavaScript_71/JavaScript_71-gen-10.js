  if (a + b > c && a + c > b && b + c > a) {
    let p = (a + b + c) / 2;
    return Math.sqrt(p * (p - a) * (p - b) * (p - c)).toFixed(2);
  } else {
    return -1;
  }
}



