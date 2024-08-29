  if (typeof a == 'number' && typeof b == 'number') {
    return a > b ? a : b;
  } else if (typeof a == 'string' && typeof b == 'string') {
    if (a.indexOf('.') > -1 && b.indexOf('.') > -1) {
      return parseFloat(a) > parseFloat(b) ? a : b;
    } else if (a.indexOf(',') > -1 && b.indexOf(',') > -1) {
      return parseFloat(a.replace(',', '.')) > parseFloat(b.replace(',', '.')) ? a : b;
    } else if (a.indexOf('.') > -1 && b.indexOf(',') > -1) {
      return parseFloat(a) > parseFloat(b.replace(',', '.')) ? a : b;
    } else if (b.indexOf('.') > -1 && a.indexOf(',') > -1) {
      return parseFloat(b) > parseFloat(a.replace(',', '.')) ? b : a;
    } else {
      return parseFloat(a.replace(',', '.')) > parseFloat(b) ? a : b;
    }
  } else {
    return null;
  }
}



