  for (let i = 0; i < l.length - 1; i++) {
    if (l[i] > l[i + 1]) {
      return false;
    }
  }

  for (let i = 0; i < l.length - 1; i++) {
    if (l[i] < l[i + 1]) {
      return false;
    }
  }

  return true;
}



