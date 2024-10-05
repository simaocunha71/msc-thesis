  if (a + b > c && a + c > b && b + c > a) {
    return Math.round((Math.sqrt(a * b * c * (a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4) * 100) / 100;
  } else {
    return -1;
  }
}