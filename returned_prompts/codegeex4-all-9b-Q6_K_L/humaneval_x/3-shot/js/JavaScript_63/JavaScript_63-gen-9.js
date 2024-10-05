  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 0;
  } else if (n == 2) {
    return 1;
  }

  let result = 0;
  let a = 0;
  let b = 0;
  let c = 1;

  for (let i = 3; i <= n; i++) {
    result = a + b + c;
    a = b;
    b = c;
    c = result;
  }

  return result;
}