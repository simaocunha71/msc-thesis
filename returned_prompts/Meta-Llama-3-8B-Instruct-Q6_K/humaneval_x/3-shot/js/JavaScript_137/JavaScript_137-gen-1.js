  if (typeof a === 'number' && typeof b === 'number') {
    return a > b ? a : b;
  } else if (typeof a === 'string' && typeof b === 'string') {
    a = parseFloat(a.replace(/,/g, ''));
    b = parseFloat(b.replace(/,/g, ''));
    return a > b ? a : (a === b ? null : b);
  } else if (typeof a === 'number' && typeof b === 'string') {
    return parseFloat(b.replace(/,/g, '')) > a ? b : a;
  } else {
    return parseFloat(a) > parseFloat(b) ? a : b;
  }
}