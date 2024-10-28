  if (a == b) {
    return null;
  }

  a = Number(a);
  b = Number(b);

  if (a > b) {
    return a;
  } else if (b > a) {
    return b;
  } else {
    return null;
  }
}



