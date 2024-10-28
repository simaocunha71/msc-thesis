  if  (n < 2) {
    return 0;
  }
  if  (n == 2) {
    return 1;
  }

  let a = [0, 0, 1];

  for  (let i = 3; i <= n; i++) {
    a.push(a[i - 1] + a[i - 2] + a[i - 3]);
  }

  return a[n];
}



