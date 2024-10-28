  if (a == 0) {
    return true;
  } else {
    let b = Math.abs(a);
    let c = Math.cbrt(b);
    return Math.floor(c) == c;
  }
}