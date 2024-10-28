  if (typeof a == typeof b) {
    if (a > b) {
      return a;
    } else if (b > a) {
      return b;
    } else if (a == b) {
      return null;
    }
  } else if (typeof a == 'string' || typeof b == 'string') {
    if (typeof a == 'string' && typeof b == 'string') {
      if (a.replace(',', '.') > b.replace(',', '.')) {
        return a;
      } else if (b.replace(',', '.') > a.replace(',', '.')) {
        return b;
      } else if (a.replace(',', '.') == b.replace(',', '.')) {
        return null;
      }
    } else if (typeof a == 'string') {
      if (a.replace(',', '.') > b) {
        return a;
      } else if (b > a.replace(',', '.')) {
        return b;
      } else if (a.replace(',', '.') == b) {
        return null;
      }
    } else {
      if (a > b.replace(',', '.')) {
        return a;
      } else if (b > a.replace(',', '.')) {
        return b;
      } else if (a.replace(',', '.') == b) {
        return null;
      }
    }
  }
}



