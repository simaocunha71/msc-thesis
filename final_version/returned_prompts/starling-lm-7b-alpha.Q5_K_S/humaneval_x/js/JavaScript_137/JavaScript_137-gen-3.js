  if (typeof a === 'string' && typeof b === 'string' && a.indexOf('.') !== -1 && b.indexOf('.') !== -1) {
    a = parseFloat(a);
    b = parseFloat(b);
  }

  if (typeof a === 'string' && typeof b === 'string' && a.indexOf(',') !== -1 && b.indexOf(',') !== -1) {
    a = parseFloat(a.replace(',', '.'));
    b = parseFloat(b.replace(',', '.'));
  }

  if (a === b) {
    return null;
  }

  return a > b ? a : b;
}



