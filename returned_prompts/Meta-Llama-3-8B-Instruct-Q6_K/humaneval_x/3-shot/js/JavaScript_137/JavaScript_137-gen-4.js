  if (typeof a === 'string') {
    a = parseFloat(a.replace(/,/g, ''));
  }
  if (typeof b === 'string') {
    b = parseFloat(b.replace(/,/g, ''));
  }
  if (a > b) {
    return a;
  } else if (a < b) {
    return b;
  } else {
    return null;
  }
}