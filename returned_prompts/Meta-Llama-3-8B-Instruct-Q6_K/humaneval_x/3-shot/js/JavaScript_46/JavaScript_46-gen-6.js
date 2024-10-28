  let a = 0;
  let b = 0;
  let c = 2;
  let d = 0;

  for (let i = 4; i <= n; i++) {
    let temp = a + b + c + d;
    a = b;
    b = c;
    c = d;
    d = temp;
  }

  return d;
}