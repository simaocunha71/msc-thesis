  for (let i = 0; i < a.length; i++) {
    if (a.indexOf(b) != -1 || a.indexOf(b + a.slice(0, i)) != -1) {
      return true;
    }
  }
  return false;
}