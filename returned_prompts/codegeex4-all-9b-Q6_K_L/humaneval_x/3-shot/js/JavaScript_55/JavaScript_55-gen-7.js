  if (n <= 0) {
    throw new Error('Input must be positive');
  }

  if (n == 1) {
    return 1;
  } else if (n == 2) {
    return 1;
  } else {
    let a = 1;
    let b = 1;
    let result = 0;
    for (let i = 3; i <= n; i++) {
      result = a + b;
      a = b;
      b = result;
    }
    return result;
  }
}



