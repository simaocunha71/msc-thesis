  if (typeof a === 'string' && typeof b === 'number') {
    a = parseFloat(a.replace(',', ''));
  } else if (typeof a === 'number' && typeof b === 'string') {
    b = parseFloat(b.replace(',', ''));
  }
  if (a > b) {
    return a;
  } else if (a < b) {
    return b;
  } else {
    return null;
  }
}