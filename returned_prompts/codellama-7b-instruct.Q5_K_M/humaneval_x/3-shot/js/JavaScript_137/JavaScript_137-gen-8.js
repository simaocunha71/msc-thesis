  if (typeof a === 'string' && typeof b === 'string') {
    const a_float = parseFloat(a.replace(',', '.'));
    const b_float = parseFloat(b.replace(',', '.'));
    if (a_float > b_float) return a;
    if (a_float < b_float) return b;
    return null;
  }

  if (typeof a === 'number' && typeof b === 'number') {
    if (a > b) return a;
    if (a < b) return b;
    return null;
  }

  if (typeof a === 'number' && typeof b === 'string') {
    if (a > parseFloat(b)) return a;
    if (a < parseFloat(b)) return b;
    return null;
  }

  if (typeof a === 'string' && typeof b === 'number') {
    if (parseFloat(a) > b) return a;
    if (parseFloat(a) < b) return b;
    return null;
  }

  if (typeof a === 'object' && typeof b === 'object') {
    if (a > b) return a;
    if (a < b) return b;
    return null;
  }
}



