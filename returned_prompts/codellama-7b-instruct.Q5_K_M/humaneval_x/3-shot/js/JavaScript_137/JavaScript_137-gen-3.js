  if (typeof a == typeof b) {
    if (a > b) return a;
    else if (a < b) return b;
    else return null;
  } else if (typeof a == 'number' && typeof b == 'string') {
    if (a > parseFloat(b)) return a;
    else if (parseFloat(b) > a) return parseFloat(b);
    else return null;
  } else if (typeof a == 'string' && typeof b == 'number') {
    if (parseFloat(a) > b) return parseFloat(a);
    else if (b > parseFloat(a)) return b;
    else return null;
  }
}



