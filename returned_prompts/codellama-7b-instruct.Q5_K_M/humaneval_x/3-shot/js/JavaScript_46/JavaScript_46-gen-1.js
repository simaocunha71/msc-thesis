  if (n == 0) {
    return 0;
  }

  var a = 0;
  var b = 0;
  var c = 2;

  for (let i = 0; i < n; i++) {
    let temp = a;
    a = b + c + a;
    b = c;
    c = temp;
  }

  return a;
}



