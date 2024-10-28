  if (n <= 1) {
    return n;
  }
  let a = 1;
  let b = 1;
  for (let i = 2; i < n; i++) {
    let temp = a;
    a = b;
    b = temp + b;
  }
  return b;
}...



