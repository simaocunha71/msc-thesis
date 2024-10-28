  if (typeof a == 'string') {
    a = parseFloat(a.replace(',', '.'));
  }

  if (typeof b == 'string') {
    b = parseFloat(b.replace(',', '.'));
  }

  if (a > b) {
    return a;
  } else if (b > a) {
    return b;
  } else {
    return null;
  }
}



