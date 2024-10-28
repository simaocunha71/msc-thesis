  if (n == 1) {
    return 2;
  }

  var count = 2;
  for (let i = 0; i < n - 2; i++) {
    count *= 9;
  }
  return count * 2;
}



