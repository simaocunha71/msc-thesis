  if (typeof a === 'number' && typeof b === 'number') {
    return (a > b) ? a : (a < b) ? b : null;
  } else if (typeof a === 'string' && typeof b === 'string') {
    return (a > b) ? a : (a < b) ? b : null;
  } else if (typeof a === 'number' && typeof b === 'string') {
    return (a > parseFloat(b.replace(/,/g, ''))) ? a : (a < parseFloat(b.replace(/,/g, ''))) ? b : null;
  } else if (typeof a === 'string' && typeof b === 'number') {
    return (parseFloat(a.replace(/,/g, '')) > b) ? a : (parseFloat(a.replace(/,/g, '')) < b) ? b : null;
  }
}