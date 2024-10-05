  if (a + b > c && a + c > b && b + c > a) {
    return (Math.sqrt(a * b * c) * (a + b + c) / 4).toFixed(2);
  } else {
    return -1;
  }
}