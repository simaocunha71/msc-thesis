  if (n == 0 || n == 1) {
    return 0;
  } else if (n == 2) {
    return 1;
  } else {
    let first = 0;
    let second = 0;
    let third = 1;
    let result = 0;
    for (let i = 3; i <= n; i++) {
      result = first + second + third;
      first = second;
      second = third;
      third = result;
    }
    return result;
  }
}