  if (typeof a === 'number' && typeof b === 'number') {
    return a > b ? a : b === a ? null : b;
  } else if (typeof a === 'string' && typeof b === 'string' && a.includes('.') && b.includes('.')) {
    return parseFloat(a) > parseFloat(b) ? a : b === parseFloat(a) ? null : b;
  } else if (typeof a === 'string' && typeof b === 'string' && !a.includes('.') && !b.includes('.')) {
    return a > b ? a : b === a ? null : b;
  } else if (typeof a === 'string' && typeof b === 'number') {
    return parseFloat(a) > b ? a : b === parseFloat(a) ? null : b;
  } else if (typeof a === 'number' && typeof b === 'string') {
    return a > parseFloat(b) ? a : b === parseFloat(a) ? null : parseFloat(b);
  }
}



