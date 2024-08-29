  for (let i = 1; i < l.length; i++) {
    if (l[i] > l[i - 1]) {
      return false;
    } else if (l[i] < l[i - 1]) {
      return false;
    }
  }
  return true;
}



