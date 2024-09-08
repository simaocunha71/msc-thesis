  if (typeof a === 'string' && typeof b === 'string') {
    return (parseFloat(a) > parseFloat(b)) ? a : (parseFloat(a) < parseFloat(b)) ? b : null;
  }
  if (typeof a === 'string' && typeof b === 'number') {
    return (parseFloat(a) > b) ? a : (parseFloat(a) < b) ? b : null;
  }
  if (typeof a === 'number' && typeof b === 'string') {
    return (a > parseFloat(b)) ? a : (a < parseFloat(b)) ? b : null;
  }
  if (typeof a === 'number' && typeof b === 'number') {
    return (a > b) ? a : (a < b) ? b : null;
  }
}



