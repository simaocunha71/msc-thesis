  if (typeof a === 'number' && typeof b === 'number') {
    return a > b ? a : b;
  } else if (typeof a === 'string' && typeof b === 'string') {
    return a > b ? a : b;
  } else if (typeof a === 'number' && typeof b === 'string') {
    return parseFloat(b) > a ? parseFloat(b) : a;
  } else if (typeof a === 'string' && typeof b === 'number') {
    return parseFloat(a) > b ? parseFloat(a) : b;
  }
  return null;
}



