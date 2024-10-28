  if (typeof a === 'number' && typeof b === 'number') {
    return (a > b) ? a : (a < b) ? b : null;
  } else if (typeof a === 'string' && typeof b === 'string') {
    a = parseFloat(a.replace(/,/g, '.')); // replace comma with dot
    b = parseFloat(b.replace(/,/g, '.')); // replace comma with dot
    return (a > b) ? a : (a < b) ? b : null;
  } else {
    return null;
  }
}