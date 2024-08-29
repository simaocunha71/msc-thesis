  if (typeof a === 'string') {
    a = parseFloat(a);
  }
  if (typeof b === 'string') {
    b = parseFloat(b);
  }

  if (a > b) {
    return a;
  } else if (b > a) {
    return b;
  } else {
    return null;
  }
}



