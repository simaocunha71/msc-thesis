  if (typeof a === 'number' && typeof b === 'number') {
    return b > a ? b : a;
  } else if (typeof a === 'string' && typeof b === 'string') {
    a = parseFloat(a.replace(',', '.'));
    b = parseFloat(b.replace(',', '.'));
    return b > a ? b : a;
  } else if (typeof a === 'number' && typeof b === 'string') {
    a = a;
    b = parseFloat(b.replace(',', '.'));
    return b > a ? b : a;
  } else if (typeof a === 'string' && typeof b === 'number') {
    a = parseFloat(a.replace(',', '.'));
    b = b;
    return b > a ? b : a;
  } else {
    return null;
  }
}