  if (typeof a === typeof b) {
    if (a > b) {
      return a;
    } else if (a < b) {
      return b;
    } else {
      return null;
    }
  } else if (typeof a === 'string') {
    a = parseFloat(a.replace(',', '.'));
    if (a > b) {
      return a;
    } else if (a < b) {
      return b;
    } else {
      return null;
    }
  } else if (typeof b === 'string') {
    b = parseFloat(b.replace(',', '.'));
    if (a > b) {
      return a;
    } else if (a < b) {
      return b;
    } else {
      return null;
    }
  }
}



