  if (typeof a === 'number' && typeof b === 'number') {
    return Math.max(a, b);
  } else if (typeof a === 'string' && typeof b === 'string') {
    a = parseFloat(a.replace(',', '.'));
    b = parseFloat(b.replace(',', '.'));
    if (a === b) {
      return null;
    } else if (a > b) {
      return a;
    } else {
      return b;
    }
  } else if (typeof a === 'number' && typeof b === 'string') {
    a = parseFloat(a);
    b = parseFloat(b.replace(',', '.'));
    if (a === b) {
      return null;
    } else if (a > b) {
      return a;
    } else {
      return b;
    }
  } else if (typeof a === 'string' && typeof b === 'number') {
    a = parseFloat(a.replace(',', '.'));
    b = parseFloat(b);
    if (a === b) {
      return null;
    } else if (a > b) {
      return a;
    } else {
      return b;
    }
  }
}