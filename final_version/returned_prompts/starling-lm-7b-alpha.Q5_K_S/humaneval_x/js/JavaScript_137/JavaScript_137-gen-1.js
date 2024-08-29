  if (typeof a === 'string' && typeof b === 'string') {
    if (a.length > 1 && a[0] === '0' && a.slice(1) === ',') {
      a = parseFloat(a.slice(1));
    } else if (a.length > 1 && a[0] === '0' && a.slice(1) === '.') {
      a = parseFloat(a.slice(1));
    } else if (a.includes(',')) {
      a = parseFloat(a.replace(',', '.'));
    }
    if (b.length > 1 && b[0] === '0' && b.slice(1) === ',') {
      b = parseFloat(b.slice(1));
    } else if (b.length > 1 && b[0] === '0' && b.slice(1) === '.') {
      b = parseFloat(b.slice(1));
    } else if (b.includes(',')) {
      b = parseFloat(b.replace(',', '.'));
    }
  }

  if (typeof a === 'number' && typeof b === 'number') {
    if (Math.abs(a - b) < 0.0000000000000001) {
      return null;
    } else if (a > b) {
      return a;
    } else {
      return b;
    }
  } else if (typeof a === 'string' && typeof b === 'number') {
    return b;
  } else if (typeof a === 'number' && typeof b === 'string') {
    return a;
  }
}



