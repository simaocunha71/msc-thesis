  if (typeof a == typeof b && typeof a == 'number') {
    return a > b ? a : b;
  } else if (typeof a == typeof b && typeof a == 'string') {
    if (a.includes(',') && b.includes(',')) {
      return parseFloat(a) > parseFloat(b) ? a : b;
    } else if (a.includes(',') && !b.includes(',')) {
      return parseFloat(a) > b ? a : b;
    } else if (!a.includes(',') && b.includes(',')) {
      return parseFloat(b) > a ? b : a;
    } else if (parseFloat(a) > parseFloat(b)) {
      return a;
    } else if (parseFloat(a) < parseFloat(b)) {
      return b;
    } else {
      return null;
    }
  } else {
    return null;
  }
}



