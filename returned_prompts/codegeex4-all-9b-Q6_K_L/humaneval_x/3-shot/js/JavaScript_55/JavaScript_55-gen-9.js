  if (n <= 1) {
    return n;
  }

  var a = 0;
  var b = 1;

  for (let i = 1; i < n; i++) {
    let temp = a;
    a = b;
    b = temp + b;
  }

  return b;
}



