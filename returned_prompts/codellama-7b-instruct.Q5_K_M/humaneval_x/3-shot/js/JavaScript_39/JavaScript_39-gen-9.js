  var a = 0;
  var b = 1;
  for (let i = 0; i < n; i++) {
    let c = a + b;
    let is_prime = true;
    for (let j = 2; j < c; j++) {
      if (c % j == 0) {
        is_prime = false;
        break;
      }
    }
    if (is_prime) {
      return c;
    }
    a = b;
    b = c;
  }
  return null;
}



