  // ...
  let y = 0;
  let z = 0;
  let r = "";
  let p = 1;
  while (x != 0) {
    z = x % base;
    x = Math.floor(x / base);
    y = y + (z * p);
    p = p * 10;
  }
  while (y != 0) {
    z = y % 10;
    y = Math.floor(y / 10);
    r = r + z;
  }
  return r;
}
  /*
  y is the quotient of x / base.
  z is the remainder of x % base.
  p is the power of 10.
  */
  return "111";
}

