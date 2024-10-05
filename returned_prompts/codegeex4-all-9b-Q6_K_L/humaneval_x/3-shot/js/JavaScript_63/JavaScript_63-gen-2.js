  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 0;
  } else if (n == 2) {
    return 1;
  } else {
    let result = 0;
    let n1 = 0;
    let n2 = 0;
    let n3 = 1;
    for (let i = 3; i <= n; i++) {
      result = n1 + n2 + n3;
      n1 = n2;
      n2 = n3;
      n3 = result;
    }
    return result;
  }
}