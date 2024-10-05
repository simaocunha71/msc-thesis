  if (a + b > c && b + c > a && c + a > b) {
    return Math.round((a * b * c) ** (1/2) * 100) / 100;
  } else {
    return -1;
  }
}



